import unittest
import requests
import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from db_fixture import test_data
import pytest


def setup_function(self):
    self.base_url = 'http://127.0.0.1:8000/api/add_event/'


def teardown_function(self):
    print(self.result)


class TestAddEvent:
    """添加发布会"""

    def test_add_event_all_null(self):
        """所有参数为空"""
        base_url = 'http://127.0.0.1:8000/api/add_event/'
        payload = {'eid': '', 'limit': '', 'address': '', 'start_time': ''}
        r = requests.post(base_url, data=payload)
        result = r.json()
        assert result['status'] == 10021
        assert result['message'] == 'parameter error'

    def test_add_event_eid_exist(self):
        """id已经存在"""
        base_url = 'http://127.0.0.1:8000/api/add_event/'
        payload = {'eid': 1, 'name': '华为发布会', 'limit': 20000, 'address': '深圳',
                   'start_time': '2019-08-22T15:16:19'}
        r = requests.post(base_url, data=payload)
        result = r.json()
        assert result['status'] == 10022
        assert result['message'] == 'event is already exists'

    def test_add_event_name_exist(self):
        """名称已经存在"""
        base_url = 'http://127.0.0.1:8000/api/add_event/'
        payload = {'eid': 6, 'name': '华为发布会', 'limit': 299, 'address': '北京',
                   'start_time': '2019-10-22T15:16:19'}
        r = requests.post(base_url, data=payload)
        result = r.json()
        assert result['status'] == 10023
        assert result['message'] == 'event name already exists'

    def test_add_event_data_type_error(self):
        """日期格式错误"""
        base_url = 'http://127.0.0.1:8000/api/add_event/'
        payload = {'eid': 6, 'name': 'iphone发布会', 'limit': 1000, 'address': '旧金山',
                   'start_time': '2017'}
        r = requests.post(base_url, data=payload)
        result = r.json()
        assert result['status'] == 10024
        assert result['message'] == 'start_time format error.It must be in YYYY-MM-DD HH:MM:SS format'

    def test_add_event_success(self):
        """添加发布会成功"""
        base_url = 'http://127.0.0.1:8000/api/add_event/'
        payload = {'eid': 10, 'name': 'iphone 11发布会', 'limit': 5000, 'address': '洛杉矶',
                   'status': 1, 'start_time': '2019-10-11T01:00:00'}
        r = requests.post(base_url, data=payload)
        result = r.json()
        assert result["status"] == 200
        assert result["message"] == 'add event success'


'''
if __name__ == '__main__':
    test_data.init_data()  # 初始化接口测试数据
    unittest.main()
'''

