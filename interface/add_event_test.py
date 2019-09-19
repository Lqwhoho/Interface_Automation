import unittest
import requests
import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from db_fixture import test_data


class AddEventTest(unittest.TestCase):
    """添加发布会"""
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/add_event/'

    def tearDown(self):
        print(self.result)

    def test_add_event_all_null(self):
        """所有参数为空"""
        payload = {'eid': '', 'limit': '', 'address': '', 'start_time': ''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_add_event_eid_exist(self):
        """id已经存在"""
        payload = {'eid': 1, 'name': '华为发布会', 'limit': 20000, 'address': '深圳',
                   'start_time': '2019-08-22T15:16:19'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event is already exists')

    def test_add_event_name_exist(self):
        """名称已经存在"""
        payload = {'eid': 6, 'name': '华为发布会', 'limit': 299, 'address': '北京',
                   'start_time': '2019-10-22T15:16:19'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')

    def test_add_event_data_type_error(self):
        """日期格式错误"""
        payload = {'eid': 6, 'name': 'iphone发布会', 'limit': 1000, 'address': '旧金山',
                   'start_time': '2017'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertEqual(self.result['message'],
                         'start_time format error.It must be in YYYY-MM-DD HH:MM:SS format')

    def test_add_event_success(self):
        """添加发布会成功"""
        payload = {'eid': 10, 'name': 'iphone 11发布会', 'limit': 5000, 'address': '洛杉矶',
                   'status': 1, 'start_time': '2019-10-11T01:00:00'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], 200)
        self.assertEqual(self.result["message"], 'add event success')


if __name__ == '__main__':
    test_data.init_data()  # 初始化接口测试数据
    unittest.main()
