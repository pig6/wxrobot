from wxpy import *

import wx_reply
import wx_command
import load


# 微信机器人，缓存登录信息
# 如果你需要部署在服务器中，则在下面加入一个入参console_qr=True
# console_qr表示在控制台打出二维码，部署到服务器时需要加上
bot = Bot(cache_path=True)
# 加载配置信息到机器人
load.load_config_to_bot(bot)


"""好友功能"""
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    """自动接受好友请求"""
    wx_reply.auto_accept_friends(msg)


@bot.register(chats=Friend)
def friend_msg(msg):
    """接收好友消息"""
    if not msg.bot.is_friend_auto_reply:
        return None
    if msg.type == TEXT:
        wx_reply.auto_reply(msg)
        return None
    elif msg.type == RECORDING:
        return '不停不停，王八念经'
    else:
        pass


"""群功能"""
@bot.register(chats=Group)
def group_msg(msg):
    """接收群消息"""
    # 群@转发功能
    if msg.is_at and msg.bot.is_forward_group_at_msg:
        msg.forward(msg.bot.master, prefix='「{0}」在群「{1}」中艾特了你：'.format(msg.member.name, msg.chat.name))

    if msg.type == TEXT:
        # 群回复
        if msg.bot.is_group_reply:
            if msg.bot.is_group_at_reply:
                # @机器人才回复
                if msg.is_at:
                    wx_reply.auto_reply(msg)
            else:
                # 不用@直接回复
                wx_reply.auto_reply(msg)
    elif msg.type == SHARING and msg.bot.is_listen_sharing and msg.chat in msg.bot.listen_sharing_groups:
        # 群分享转发监控，防止分享广告
        msg.forward(msg.bot.master, prefix='分享监控：「{0}」在「{1}」分享了：'.format(msg.member.name, msg.chat.name))
    else:
        pass
    # 监听好友群聊，如老板讲话
    if msg.bot.is_listen_friend and msg.chat in msg.bot.listen_friend_groups and msg.member.is_friend in msg.bot.listen_friends:
        msg.forward(msg.bot.master, prefix='监听指定好友群消息：「{0}」在「{1}」发了消息：'.format(msg.member.is_friend.remark_name or msg.member.nick_name, msg.chat.name))
    return None


@bot.register(msg_types=NOTE)
def system_msg(msg):
    """接收系统消息"""
    wx_reply.handle_system_msg(msg)


"""管理员功能"""
@bot.register(chats=bot.master)
def do_command(msg):
    """执行管理员命令"""
    wx_command.do_command(msg)


# 堵塞进程，直到结束消息监听 (例如，机器人被登出时)
# embed() 互交模式阻塞，电脑休眠或关闭互交窗口则退出程序
bot.join()