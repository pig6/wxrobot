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


def handle_system_msg(msg):
    """处理系统消息"""
    raw = msg.raw
    # 4表示消息状态为撤回
    if raw['Status'] == 4 and msg.bot.is_forward_revoke_msg:
        # 转发撤回的消息
        forward_revoke_msg(msg)


def forward_revoke_msg(msg):
    """转发撤回的消息"""
    # 获取被撤回消息的ID
    revoke_msg_id = re.search('<msgid>(.*?)</msgid>', msg.raw['Content']).group(1)
    # bot中有缓存之前的消息，默认200条
    for old_msg_item in msg.bot.messages[::-1]:
        # 查找撤回的那条
        if revoke_msg_id == str(old_msg_item.id):
            # 判断是群消息撤回还是好友消息撤回
            if old_msg_item.member:
                sender_name = '群「{0}」中的「{1}」'.format(old_msg_item.chat.name, old_msg_item.member.name)
            else:
                sender_name = '「{}」'.format(old_msg_item.chat.name)
            # 名片无法转发
            if old_msg_item.type == 'Card':
                sex = '男' if old_msg_item.card.sex == 1 else '女' or '未知'
                msg.bot.master.send('「{0}」撤回了一张名片：\n名称：{1}，性别：{2}'.format(sender_name, old_msg_item.card.name, sex))
            else:
                # 转发被撤回的消息
                old_msg_item.forward(msg.bot.master,
                                     prefix='{}撤回了一条消息：'.format(sender_name, get_msg_chinese_type(old_msg_item.type)))
            return None


def get_msg_chinese_type(msg_type):
    """转中文类型名"""
    if msg_type == 'Text':
        return '文本'
    if msg_type == 'Map':
        return '位置'
    if msg_type == 'Card':
        return '名片'
    if msg_type == 'Note':
        return '提示'
    if msg_type == 'Sharing':
        return '分享'
    if msg_type == 'Picture':
        return '图片'
    if msg_type == 'Recording':
        return '语音'
    if msg_type == 'Attachment':
        return '文件'
    if msg_type == 'Video':
        return '视频'
    if msg_type == 'Friends':
        return '好友请求'
    if msg_type == 'System':
        return '系统'
