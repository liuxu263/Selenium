# -*- coding: UTF-8 -*-
from Python.Web_UI.driver import Driver
from Python.Web_UI.common.common import click
from Python.Web_UI.common.common import find
from Python.Web_UI.common.common import get_url
import unittest


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
