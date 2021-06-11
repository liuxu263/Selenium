#! /user/bin/env python
# -*- coding: utf-8 -*-

import requests


def test():
    url = "xxx"
    headers = {"xx": "xx"}
    r = requests.get(url, headers=headers)
    r = r.json()
    pass
