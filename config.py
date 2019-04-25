"""项目配置"""

# 图灵机器人，99元一月付费版，尽情享用！
tuling_api_key = '88f17f853d974387af64955bed9466f4'

# 自动回复
is_friend_auto_reply = True
is_group_reply = True  # 此项表示群中是否回复
is_group_at_reply = True  # 上一项开启后此项才生效

# 机器人主人
bot_master_remark_name = '猪哥'  # 使用备注名更安全，只允许一个
bot_master_signature = '男友与猫'  # 签名

# 监听老板
is_listen_boss = False
boss_remark_name = '猪哥'  # 需要监听的人的备注名，使用备注名更安全
listen_boss_groups = '唯一集团工作群'  # 在这些群里监听老板说的话，匹配模式：包含“唯一集团工作群”的群


# 转发信息至群
is_forward_mode = False  # 打开转发模式，主人发送给机器人的消息都将转发至forward_groups群
forward_groups = '唯一集团工作群'  # 需要将消息转发的群，匹配模式同上

# 群分享监控
is_listen_sharing = False
listen_sharing_groups = '唯一集团工作群'  # 监控群分享，匹配模式同上


