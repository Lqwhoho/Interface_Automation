import time
import sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
import HTMLTestRunner_cn
import unittest
from db_fixture import test_data
import pytest

# 指定测试用例位当前文件下的interface目录
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')


if __name__ == "__main__":
    test_data.init_data()  # 初始化接口测试数据
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, description=u'运行环境：MySQL(PyMySQL), Requests, unittest ',
                                              title=u'发布会签到系统接口自动化测试')
    runner.run(discover)
    fp.close()

