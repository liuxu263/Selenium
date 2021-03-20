# -*- coding: UTF-8 -*-

from python.web_ui.testsuites.testsuite2 import TestSuite2
import unittest

if __name__ == '__main__':
    suite = TestSuite2().suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
