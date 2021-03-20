# -*- coding: UTF-8 -*-
from python.web_ui.driver import Driver
from python.web_ui.common.common import click
from python.web_ui.common.common import find
from python.web_ui.common.common import get_url
from python.web_ui.testdatas.baidu_home_page_data import baidu_home_page_data
import unittest


class Test1(unittest.TestCase):
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
        find(self.driver, "百度首页", "搜索输入框").send_keys(baidu_home_page_data.get("111"))
        click(self.driver, "百度首页", "百度一下按钮")
        find(self.driver, "百度搜索结果页", "搜索结果")

    def test2(self):
        pass
