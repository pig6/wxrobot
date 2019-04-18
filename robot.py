from wxpy import *

import wx_friend
import baidu_transition

# 微信机器人，缓存登录信息
bot = Bot(cache_path=True)


@bot.register(chats=Friend, msg_types=TEXT)
def auto_reply(msg):
    """自动回复"""
    # if msg.type == TEXT:
    # wx_friend.auto_reply(msg)
    # elif msg.type == RECORDING:
    #     baidu_transition


@bot.register(chats=Friend, msg_types=RECORDING)
def auto_reply(msg):
    text_msg = baidu_transition.voice_to_text(msg)
    wx_friend.auto_reply(text_msg)


embed()

