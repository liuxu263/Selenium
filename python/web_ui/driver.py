# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
import os


class Driver(object):
    def __init__(self):
        # path_chrome_driver = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config/chromedriver")
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option()
        # desired_capabilities = webdriver.DesiredCapabilities.CHROME
        # desired_capabilities[xx] = {'xx': 'xx'}
        # self.driver = webdriver.Chrome(executable_path=path_chrome_driver,
        #                                options=options,
        #                                desired_capabilities=desired_capabilities)
        self.driver.implicitly_wait(5)
        self.driver = webdriver.Chrome()

    def init_driver(self):
        self.driver.fullscreen_window()
        time.sleep(2)
        return self.driver
