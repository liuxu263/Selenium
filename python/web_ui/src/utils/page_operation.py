#! /user/bin/env python
# -*- coding:utf-8 -*-


import os
import time

from selenium.common.exceptions import NoSuchElementException

from python.web_ui.src.pages_locators.ui import ui
from python.web_ui.src.testcases.testdata import data_common


# 截图
def shot_screen(self, method_name, pic_name):
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    path = base_path + "/output/" + data_common.time + "/" + self.class_name + "/" + method_name
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = path + "/" + pic_name + ".png"
    try:
        self.driver.get_screenshot_as_file(file_name)
    except OSError:
        print('截图失败')


def by(page, element):
    return ui.get(page).get(element)[0]


def value(page, element):
    return ui.get(page).get(element)[1]


# 查找元素
def find(driver, page, element):
    return driver.find_element(by(page, element), value(page, element))


# 点击元素
def click(driver, page, element):
    try:
        time.sleep(0.5)
        find(driver, page, element).click()
        time.sleep(0.5)
    except NoSuchElementException:
        raise
