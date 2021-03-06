#! /usr/bin/python
# -*- coding:utf-8 -*-

import requests

class HTTP(object):
    # 静态方法
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # 三元表达式
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''