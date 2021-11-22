#! /user/bin/env python
# -*- coding:utf-8 -*-

from python.web_ui.src.pages_locators.page1 import page_baidu_home
from python.web_ui.src.pages_locators.page2 import page_baidu_search_results
from python.web_ui.src.pages_locators.page3 import page_baidu_login_in

ui = {
    "百度首页": page_baidu_home,
    "百度登录页": page_baidu_login_in,
    "百度搜索结果页": page_baidu_search_results
}
