#! /user/bin/env python
# -*- coding:utf-8 -*-

import unittest
import time
import multiprocessing
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

    send_alert("用例执行开始")
    start_time = datetime.now()
    print("开始时间:" + time.strftime("%Y_%m_%d_%H:%M:%S", time.localtime()))

    process1 = multiprocessing.Process(target=run_test_suite, args=(test_suite1(),))
    process2 = multiprocessing.Process(target=run_test_suite, args=(test_suite2(),))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    send_alert("用例执行结束")
    end_time = datetime.now()
    print("结束时间:" + time.strftime("%Y_%m_%d_%H:%M:%S", time.localtime()))
    print("用时:" + str((end_time - start_time).seconds) + "s")


def run_test_suite(test_suite):
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)


if __name__ == '__main__':
    launch()
