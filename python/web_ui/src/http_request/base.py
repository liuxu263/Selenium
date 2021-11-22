#! /user/bin/env python
# -*- coding:utf-8 -*-

import requests


class HttpRequest(object):
    def __init__(self):
        self.session = requests.session()

    def http_request(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        return self.session.request(method, url, params, data, json, headers, **kwargs)

    def close_session(self):
        self.session.close()
