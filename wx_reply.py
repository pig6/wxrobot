# 好友功能
import re

import tuling_robot


def auto_accept_friends(msg):
    """自动接受好友"""
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('我已自动接受了你的好友请求')


def auto_reply(msg):
    """自动回复"""
    # 关键字回复 or 图灵机器人回复
    # handle_withdraw_msg(msg)
    keyword_reply(msg) or tuling_reply(msg)


def keyword_reply(msg):
    """关键字回复"""
    if '你叫啥' in msg.text or '你叫啥名字' in msg.text:
        return msg.reply('沃德天·维森莫·拉莫帅·帅德布耀')
    pass


def tuling_reply(msg):
    """图灵机器人回复"""
    tuling_robot.auto_reply(msg)


def handle_withdraw_msg(msg):
    """测回消息"""
    raw = msg.raw
    if raw['Status'] == 4:
        # 获取被撤回消息的ID
        oldmsgid = re.search(re.compile('<msgid>(.*?)</msgid>', re.S), raw['Content']).group(1)
        for one_msg in msg.bot.messages[::-1]:  # 从后循环所有信息
            if oldmsgid == str(one_msg.id):  # 此msg就是撤回的信息
                # 根据发送者设定转发前缀
                if one_msg.member:
                    the_sender = '群[%s]中的 @%s ' % (one_msg.chat.name, one_msg.member.name)
                else:
                    the_sender = one_msg.chat.name
                # 不是名片时，直接用forward转发到文件助手
                if one_msg.type != 'Card':
                    one_msg.forward(msg.bot.file_helper, prefix='%s\n撤回了一条%s消息：' % (the_sender, one_msg.type))
                else:
                    card = one_msg.card
                    name = card.name
                    if card.sex == 1:
                        sex = '男'
                    else:
                        sex = '女'
                    msg.bot.file_helper.send('%s\n撤回了一张名片：\n名称：%s，性别：%s' % (the_sender, name, sex))
