from wxpy import *

import wx_command
import load

# 微信群直播（转发）机器人
# console_qr表示在控制台打出二维码，部署到服务器时需要加上
# 如果需要登录多个微信，则将cache_path参数去掉，然后勾选：Aalow parallel run 这样可以运行多个后台
# 一般情况一个微信可以转发消息到8-9个群，太多的话会提示发送消息过于频繁！
# 详细教程、问题反馈、意见建议，关注微信公众号：裸睡的猪
bot = Bot(cache_path=True)
load.load_config_to_bot(bot)


@bot.register(chats=Group)
def group_msg(msg):
    """接收群消息"""
    # 判断是否满足转发直播条件：开启直播模式+当前消息是主讲群内的+发消息的人是主讲人
    if msg.bot.is_live_mode and msg.chat == msg.bot.live_group and msg.member.name == msg.bot.live_speaker:
        forward_groups = wx_command.remote_forward(msg)
        msg.reply('消息发送完毕，共发送至{}个群'.format(len(forward_groups)))
    return None


@bot.register(chats=bot.master)
def do_command(msg):
    """执行管理员命令"""
    wx_command.do_command(msg)


# 堵塞进程，直到结束消息监听 (例如，机器人被登出时)
# embed() 互交模式阻塞，电脑休眠或关闭互交窗口则退出程序
bot.join()
