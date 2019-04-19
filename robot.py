from wxpy import *

import wx_friend

# 微信机器人，缓存登录信息
bot = Bot(cache_path=True)


@bot.register(msg_types=FRIENDS)
def auto_reply(msg):
    """自动接受好友请求"""
    wx_friend.auto_accept_friends(msg)


@bot.register(chats=Friend)
def auto_reply(msg):
    """自动回复好友"""
    if msg.type == TEXT:
        wx_friend.auto_reply(msg)
    elif msg.type == RECORDING:
        return '不听不听，王八念经'
    else:
        pass


embed()

