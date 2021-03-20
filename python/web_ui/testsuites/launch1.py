# -*- coding: UTF-8 -*-

from python.web_ui.testsuites.testsuite1 import TestSuite1
import unittest

if __name__ == '__main__':
    suite = TestSuite1().suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
