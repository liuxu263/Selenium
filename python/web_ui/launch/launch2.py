# -*- coding: UTF-8 -*-

import sys
import unittest
import time

from python.web_ui.testsuites.testsuite1 import test_suite1
from python.web_ui.testdata import common_data
from python.web_ui.utils.common import send_alert


def launch():
    if len(sys.argv) != 4:
        send_alert("输入参数错误")
        return

    common_data.time = time.strftime("%Y_%m_%d_%H:%M:%S", time.localtime())
    suite = test_suite1()
    runner = unittest.TextTestRunner(verbosity=2)
    send_alert("用例执行开始")
    runner.run(suite)
    send_alert("用例执行结束")


if __name__ == '__main__':
    launch()
