import random
import time

import load


def do_command(msg):
    """执行管理员命令"""
    if '开启直播模式' == msg.text:
        msg.bot.is_live_mode = True
        msg.reply(load.load_live(msg.bot))
        return None

    if '关闭直播模式' == msg.text:
        msg.bot.is_live_mode = False
        msg.reply('已关闭直播模式！')
        return None

    if '休眠' == msg.text:
        remote_down(msg)
        msg.reply('已休眠，所有功能暂停！')
        return None

    if '开启' == msg.text:
        remote_reup(msg)
        msg.reply('已开启')
        return None

    if '退出' == msg.text:
        msg.reply('机器人正在退出...')
        msg.bot.logout()
        return None

    msg.reply(f'此命令无法识别：{msg.text}')
    return None


# 开启所有注册函数
def remote_reup(msg):
    msg.bot.registered.enable()


def remote_down(msg):
    """将除远程主人监听的其他监听注销"""
    do_command_register = msg.bot.registered.get_config(msg)
    msg.bot.registered.remove(do_command_register)
    msg.bot.registered.disable()
    msg.bot.registered.append(do_command_register)


def remote_forward(msg):
    """转发消息"""
    forward_groups = []
    for group in msg.bot.forward_groups:
        msg.forward(group, suffix='')
        forward_groups.append(group.name)
        time.sleep(random.random())
    return forward_groups
