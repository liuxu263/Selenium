#! /user/bin/env python
# -*- coding:utf-8 -*-

import time
import os

from selenium import webdriver


class Driver(object):
    driver = None

    @classmethod
    def init_driver(cls):
        path_chrome_driver = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                          "config/chromedriver")
        options = webdriver.ChromeOptions()
        # options.add_experimental_option("xxx")
        desired_capabilities = webdriver.DesiredCapabilities.CHROME
        # desired_capabilities[xx] = {'xx': 'xx'}
        if cls.driver is None:
            cls.driver = webdriver.Chrome(executable_path=path_chrome_driver,
                                          options=options,
                                          desired_capabilities=desired_capabilities)
        # cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.fullscreen_window()
        time.sleep(2)
        return cls.driver