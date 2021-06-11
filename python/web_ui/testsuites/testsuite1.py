# -*- coding: UTF-8 -*-

import unittest
from python.web_ui.testcases.testcase1 import Test1
from python.web_ui.testcases.testcase2 import Test2


def test_suite1():
    suite = unittest.TestSuite()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Test1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(Test2)

    suite.addTest(suite1)
    suite.addTest(suite2)
    return suite
