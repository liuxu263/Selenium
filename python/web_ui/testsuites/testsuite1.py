# -*- coding: UTF-8 -*-
from python.web_ui.testcases.testcase1 import Test1
from python.web_ui.testcases.testcase2 import Test2
import unittest


class TestSuite1(object):
    suite = unittest.TestSuite()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Test1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(Test2)

    suite.addTest(suite1)
    suite.addTest(suite2)