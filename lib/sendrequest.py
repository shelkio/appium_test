#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import logging

from lib.signparms import SignParms
import requests


class SendRequests:
    def __init__(self):
        pass

    """发送请求数据"""
    def sendRequests(self, method, url, data):
        body_data = SignParms.sign(data,"101000001192","C7717A19F0615B0BBE07286253B9E823")
        body = json.dumps(body_data)
        logging.info("请求url: {0}".format(url))
        logging.info("请求方式: {0}".format(method))
        logging.info("请求参数: {0}".format(data))
        #发送请求
        re = requests.request(method=method,url=url,headers={'Content-Type': 'application/json;charset=UTF-8'}
,data=body)
        logging.info("返回结果" + str(re.json()))
        return re
