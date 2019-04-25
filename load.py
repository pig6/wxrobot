from wxpy import *

import config


def load_config_bot(bot):
    """加载配置项"""
    bot_status = '机器人配置信息：'
    # 定义远程管理主人 (用于远程管理)
    try:
        bot.master = ensure_one(
            bot.friends().search(remark_name=config.bot_master_remark_name, signature=config.bot_master_signature))
        bot_status += '\n机器人主人设置成功：「{0}」，这里查看管理员命令手册->：' \
                      'https://github.com/pig6/wxrobot/tree/dev-tuling#%E7%AE%A1%E7%90%86%E5%91%98%E5%8A%9F%E8%83%BD'\
                      .format(config.bot_master_remark_name)
    except ValueError:
        bot.master = bot.file_helper
        bot_status += '\n机器人主人设置未成功，信息将发送至文件助手，不能远程用命令控制机器人！'
    # 设置开关
    bot.is_friend_auto_reply = config.is_friend_auto_reply
    bot.is_group_reply = config.is_group_reply
    bot.is_group_at_reply = config.is_group_at_reply
    bot.is_listen_boss = config.is_listen_boss
    bot.is_forward_mode = config.is_forward_mode
    bot.is_listen_sharing = config.is_listen_sharing
    # 加载对应好友和群
    load_listen_boss(bot)
    load_forward_groups(bot)
    load_listen_sharing_groups(bot)
    bot.master.send(bot_status)


def load_listen_boss(bot):
    """加载老板、需要监听的群"""
    if bot.is_listen_boss:
        bot.boss = bot.friends().search(remark_name=config.boss_remark_name)
        if len(bot.boss) < 1:
            bot.boss = []
            bot.master.send('未在好友中找到备注为「{}」的监听对象！'.format(config.boss_remark_name))

        bot.listen_boss_groups = bot.groups().search(config.listen_boss_groups)
        if len(bot.listen_boss_groups) < 1:
            bot.listen_boss_groups = []
            bot.master.send('未找到群名包含「{}」的监听群！'.format(config.listen_boss_groups))


def load_forward_groups(bot):
    """加载需要转发的群"""
    if bot.is_forward_mode:
        bot.forward_groups = bot.groups().search(config.forward_groups)
        if len(bot.forward_groups) < 1:
            bot.master.send('未找到群名包含「{}」的转发群！'.format(config.forward_groups))


def load_listen_sharing_groups(bot):
    """加载监控群"""
    if bot.is_listen_sharing:
        bot.listen_sharing_groups = bot.groups().search(config.listen_sharing_groups)
        if len(bot.listen_sharing_groups) < 1:
            bot.master.send('未找到群名包含「{}」的分享监控群！'.format(config.listen_sharing_groups))


def bot_status_detail(bot):
    """机器人配置状态"""
    master_name = '机器人管理员：{0}（{1})）'.format(bot.master.name, bot.master.remark_name)
    friend_auto_reply = '\n好友自动回复：{}'.format(('是' if bot.is_friend_auto_reply else '否'))
    group_reply = '\n群聊回复：{}'.format(('是，是否需要@才回复：{}'.format(('是' if bot.is_group_at_reply else '否')) if bot.is_group_reply else '否'))
