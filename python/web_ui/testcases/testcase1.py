# -*- coding: UTF-8 -*-

import unittest
import time

from python.web_ui.driver import Driver
from python.web_ui.utils.page_operation import click
from python.web_ui.utils.page_operation import find
from python.web_ui.utils.common import get_url
from python.web_ui.utils.page_operation import shot_screen
from python.web_ui.testdata import baidu_home_page_data


class Test1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.class_name = cls.__name__.lower()
        driver = Driver()
        cls.url = get_url()
        cls.driver = driver.init_driver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        self.driver.get(self.url)

    def tearDown(self) -> None:
        pass

    def test1(self):
        shot_screen(self, self.test1.__name__, "1")
        find(self.driver, "百度首页", "搜索输入框").send_keys(baidu_home_page_data.test)
        click(self.driver, "百度首页", "百度一下按钮")
        find(self.driver, "百度搜索结果页", "搜索结果")

    def test2(self):
        pass
