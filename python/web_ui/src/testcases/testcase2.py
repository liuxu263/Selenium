#! /user/bin/env python
# -*- coding:utf-8 -*-

import unittest
from python.web_ui.src.driver import Driver
from python.web_ui.src.utils.common import click
from python.web_ui.src.utils.common import find
from python.web_ui.src.utils.common import get_url



class Test2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        driver = Driver()
        cls.driver = driver.get_driver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        get_url(self.driver)

    def tearDown(self) -> None:
        pass

    def test1(self):
        pass

    def test2(self):
        click(self.driver, "百度首页", "登录按钮")
        find(self.driver, "百度登录页", "用户名登录按钮")
