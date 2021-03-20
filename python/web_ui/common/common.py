# -*- coding: UTF-8 -*-
from python.web_ui.testdatas.common_data import common_data
from python.web_ui.ui import ui
from selenium.common.exceptions import NoSuchElementException
from time import sleep


def get_url(driver):
    url = common_data.get("url")
    return driver.get(url)


def by(page, element):
    return ui.get(page).get(element)[0]


def value(page, element):
    return ui.get(page).get(element)[1]


def find(driver, page, element):
    return driver.find_element(by(page, element), value(page, element))


def click(driver, page, element):
    try:
        sleep(1)
        find(driver, page, element).click()
        sleep(1)
    except NoSuchElementException:
        raise
