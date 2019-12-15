from wxpy import *

import config

logger = logging.getLogger('itchat')


def load_config_to_bot(bot):
    """加载配置项"""
    bot_status = '直播机器人登录成功！！！'
    # 未定义机器人管理员
    if not config.bot_master:
        bot.master = bot.file_helper
        bot_status += '\n未设置机器人管理员，信息将发送至文件助手，不能使用远程命令控制机器人！\n\n'
    else:
        master = search_friend(bot, config.bot_master)
        # 查找管理员
        if master:
            bot.master = master
            bot_status += f'\n机器人管理员成功设置为：{config.bot_master}'
        else:
            bot.master = bot.file_helper
            bot_status += f'\n在好友列表中未找到名为{config.bot_master}的好友，信息将发送至文件助手，不能使用远程命令控制机器人！\n\n'

    # 加载直播信息
    live_status_detail = load_live(bot)
    bot_status += live_status_detail
    # 发送机器人状态信息
    bot.master.send(bot_status)
    logger.info(bot_status)


def load_live(bot):
    """加载需要转发的群"""
    # 设置开关
    bot.is_live_mode = config.is_live_mode
    if not bot.is_live_mode:
        return '\n未开启直播模式，可在 config.py 文件中将 is_live_mode 设置为True开启！'
    live_status_detail = ''
    # 1、加载主讲群
    live_group = bot.groups().search(config.live_group)
    if len(live_group) < 1:
        bot.live_group = None
        bot.is_live_mode = False
        return f'\n主讲群：未找到群名包含「{config.live_group}」的主讲群！\n开启群直播失败！\n\n可在主讲群中发任意消息，然后管理员使用命令：开启群直播模式，从新加载直播信息！'
    elif len(live_group) > 1:
        bot.live_group = live_group[0]
        live_status_detail += f'\n主讲群：找到多个群名包含「{config.live_group}」的主讲群，默认选取第一个群（{live_group[0]}）作为主讲群!'
    else:
        bot.live_group = live_group[0]

    # 2、加载主讲人
    live_group_members = bot.live_group.members
    for member in live_group_members:
        if member.name == config.live_speaker:
            live_status_detail += f'\n主讲人：「{config.live_speaker}」'
            bot.live_speaker = config.live_speaker
            break
    else:
        live_status_detail += f'\n主讲人：主讲群内未找到主讲人「{config.live_speaker}」。\n开启群直播失败！'
        bot.is_live_mode = False
        return live_status_detail

    # 3、加载转发群
    forward_groups = search_groups(bot, config.forward_groups)
    bot.forward_groups = forward_groups
    live_status_detail += f'\n转发群：消息将会转发至这些群：{str(forward_groups)}，共{len(forward_groups)}个。\n\n如有遗漏可在这些群中发任意消息，然后管理员使用命令：开启群直播模式，从新加载直播信息！'
    return live_status_detail


def search_friend(bot, name):
    """查找某个好友
    优先级为：好友备注-好友昵称
    """
    nick_name_friend = None
    for friend in bot.friends():
        if getattr(friend, 'remark_name', None) == name:
            return friend
        elif not nick_name_friend and getattr(friend, 'nick_name', None) == name:
            nick_name_friend = friend
    return nick_name_friend or None


def search_groups(bot, names):
    """
    查找多个群，用|分割
    """
    split_names = names.split('|')
    result_list = []
    for group in split_names:
        result_group = bot.groups().search(group)
        if len(result_group) > 0:
            result_list.extend(result_group)
    return result_list
