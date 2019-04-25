import json
import requests

from wxpy import *

import config


"""
    免费申请图灵机器人，获取api_key
    图灵机器人免费申请地址 http://www.tuling123.com
"""
tuling = Tuling(api_key=config.tuling_api_key)


def auto_reply(msg):
    """回复消息，并返回答复文本"""
    return tuling.do_reply(msg)


if __name__ == '__main__':
    """
        直接点击测试图灵机器人
        此apikey为wxpy自带apikey，有使用次数限制，建议自己免费申请一个
        图灵机器人免费申请地址 http://www.tuling123.com
    """
    apikey = '7c8cdb56b0dc4450a8deef30a496bd4c'
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {'key': apikey, 'info': '你好'}
    req = requests.post(api_url, data=data).text
    replys = json.loads(req)['text']
    print(replys)