#! /user/bin/env python
# -*- coding:utf-8 -*-

import os
import yaml


def get_data_from_yaml(file):
    with open(file, 'r', encoding="utf-8") as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
    return content


def set_data_to_yaml(file, content):
    with open(file, 'w+', encoding="utf-8") as f:
        yaml.dump(content, f, Dumper=yaml.Dumper)


def get_url():
    url = "http://www.baidu.com"
    return url


def send_alert(message):
    print("发送报警")
    print(message)
