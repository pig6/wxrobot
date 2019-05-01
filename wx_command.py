import load


def do_command(msg):
    """执行管理员命令"""
    if '查看状态' == msg.text:
        msg.reply(load.bot_status_detail(msg.bot))
        return None

    if '关闭转发模式' == msg.text:
        msg.bot.is_forward_mode = False
        msg.reply('已关闭转发模式')
        return None

    if msg.bot.is_forward_mode:
        forward_result = remote_forward(msg)
        msg.bot.is_forward_mode = False
        msg.reply('已转发消息至：{}，自动退出转发模式！'.format(forward_result))
        return None

    if '开启好友回复' == msg.text:
        msg.bot.is_friend_auto_reply = True
        msg.reply('已开启好友回复')
        return None

    if '关闭好友回复' == msg.text:
        msg.bot.is_friend_auto_reply = False
        msg.reply('已关闭好友回复')
        return None

    if '开启群聊回复' == msg.text:
        msg.bot.is_group_reply = True
        msg.reply('已开启群聊回复')
        return None

    if '关闭群聊回复' == msg.text:
        msg.bot.is_group_reply = False
        msg.reply('已关闭群聊回复')
        return None

    if '开启群聊艾特回复' == msg.text:
        msg.bot.is_group_at_reply = True
        msg.reply('已开启群聊艾特回复')
        return None

    if '关闭群聊艾特回复' == msg.text:
        msg.bot.is_group_at_reply = False
        msg.reply('已关闭群聊艾特回复')
        return None

    if '开启转发群艾特模式' == msg.text:
        msg.bot.is_forward_group_at_msg = True
        msg.reply('已开启转发群艾特模式')
        return None

    if '关闭转发群艾特模式' == msg.text:
        msg.bot.is_forward_group_at_msg = False
        msg.reply('已关闭转发群艾特模式')
        return None

    if '开启防撤回模式' == msg.text:
        msg.bot.is_forward_revoke_msg = True
        msg.reply('已开启防撤回模式')
        return None

    if '关闭防撤回模式' == msg.text:
        msg.bot.is_forward_revoke_msg = False
        msg.reply('已关闭防撤回模式')
        return None

    if '开启监听模式' == msg.text:
        msg.bot.is_listen_friend = True
        # 重新加载配置信息
        errmsg = load.load_listen_friend(msg.bot)
        if errmsg:
            msg.reply('开启监听模式失败，{}'.format(errmsg))
        else:
            msg.reply('已开启监听模式，在{0}中监听{1}'.format(str(msg.bot.listen_friend_groups), str(msg.bot.listen_friends)))
        return None

    if '关闭监听模式' == msg.text:
        msg.msg.bot.is_listen_friend = False
        msg.reply('已关闭监听模式')
        return None

    if '开启监控模式' == msg.text:
        msg.bot.is_listen_sharing = True
        # 重新加载配置信息
        errmsg = load.load_listen_sharing_groups(msg.bot)
        if errmsg:
            msg.reply('开启群分享监控失败，{}'.format(errmsg))
        else:
            msg.reply('已开启群分享监控，将监控这些群：{}'.format(str(msg.bot.listen_sharing_groups)))
        return None

    if '关闭监控模式' == msg.text:
        msg.bot.is_listen_sharing = False
        msg.reply('已关群分享监控')
        return None

    if '开启转发模式' == msg.text:
        msg.bot.is_forward_mode = True
        # 重新加载配置信息
        errmsg = load.load_forward_groups(msg.bot)
        if errmsg:
            msg.reply('开启转发模式失败，{}'.format(errmsg))
        else:
            msg.reply('已开启转发模式，直接发送消息给我就会转发到这些群：{0}，如果不想转发可以对我说：{1}'.format(str(msg.bot.forward_groups), '关闭转发模式'))
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

    if '查看状态' == msg.text:
        msg.reply(load.bot_status_detail(msg.bot))
        return None

    msg.reply('此命令无法识别：{}'.format(msg.text))
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
        msg.forward(group, suffix='猪哥转发')
        forward_groups.append(group.name)
    return forward_groups
