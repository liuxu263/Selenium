# -*- coding: UTF-8 -*-
from selenium import webdriver
import time


class Driver(object):
    def __init__(self):
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option()
        self.driver = webdriver.Chrome()

    def get_driver(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(2)
        return self.driver
