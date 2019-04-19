# 好友功能
from wxpy import *
import tuling_robot

bot = Bot()


def auto_accept_friends(msg):
    """自动接受好友"""
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('我已自动接受了你的好友请求')


def auto_reply(msg):
    """自动回复"""
    # 关键字回复 or 图灵机器人回复
    keyword_reply(msg) or tuling_reply(msg)


def keyword_reply(msg):
    """关键字回复"""
    if '你叫啥' in msg.text or '你叫啥名字' in msg.text:
        return msg.reply('沃德天·维森莫·拉莫帅·帅德布耀')
    pass


def tuling_reply(msg):
    """图灵机器人回复"""
    tuling_robot.auto_reply(msg)
