#! /user/bin/env python
# -*- coding:utf-8 -*-


import unittest
import time
from datetime import datetime

from python.web_ui.src.testsuites.testsuite1 import test_suite1
from python.web_ui.src.testsuites.testsuite2 import test_suite2
from python.web_ui.src.testcases.testdata import data_common
from python.web_ui.src.utils.common import send_alert


def launch():
    # if len(sys.argv) != 4:
    #     send_alert("输入参数错误")
    #     return

    data_common.time = time.strftime("%Y_%m_%d_%H:%M:%S", time.localtime())

    runner = unittest.TextTestRunner(verbosity=2)
    send_alert("用例执行开始")
    start_time = datetime.now()
    print("开始时间:" + time.strftime("%Y_%m_%d_%H:%M:%S", time.localtime()))
    runner.run(test_suite1())
    runner.run(test_suite2())
    send_alert("用例执行结束")
    end_time = datetime.now()
    print("结束时间:" + time.strftime("%Y_%m_%d_%H:%M:%S", time.localtime()))
    print("用时:" + str((end_time - start_time).seconds) + "s")


if __name__ == '__main__':
    launch()
