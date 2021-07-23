#! /user/bin/env python
# -*- coding:utf-8 -*-


import os
import time
from selenium.common.exceptions import NoSuchElementException

from python.web_ui.src.ui import ui
from python.web_ui.src.testdata import common_data


def shot_screen(self, method_name, pic_name):
    base_path = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + '.')
    path = base_path + "/web_ui/output/" + common_data.time + "/" + self.class_name + "/" + method_name
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


def find(driver, page, element):
    return driver.find_element(by(page, element), value(page, element))


def click(driver, page, element):
    try:
        time.sleep(1)
        find(driver, page, element).click()
        time.sleep(1)
    except NoSuchElementException:
        raise
