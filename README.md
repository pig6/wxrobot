# wxrobot
基于python的微信机器人，猪哥开发环境Macos+Python3.7+Pycharm

欢迎大家在我公众号：`裸睡的猪`中给我提出建议和意见

本项目基于微信网页版API，所以需要提前测试你使用的微信是否可以登录网页版微信：https://wx.qq.com/

![裸睡的猪](https://img-blog.csdnimg.cn/20181217213155258.gif)

## 一、启动步骤
1.下载wxpy库 `pip3 install -U wxpy -i "https://pypi.doubanio.com/simple/"`，使用的是国内源，如果使用anaconda直接在pycharm里面下载，注意项目环境问题！

2.启动`robot.py`，弹出登录二维码，手机微信扫一扫登录

3.手机端同意登录，直播参数在config.py中调整

4.在robot.py中修改了bot = Bot(cache_path=True, console_qr=True)，console_qr=True表示在控制台打印二维码显示，方便部署到服务器，如果你不需要部署服务器可去掉这个入参。`cache_path`表示缓存登录信息，如果需要登录多个微信，则可以去掉该参数！


## 二、功能介绍

### 1.群直播
群直播的参数在config.py中调整。

如果出现主讲群或者转发群未加载到的情况，可以在需要加载的群里发送任意消息，然后管理员使用命令： `开启群直播模式`从新加载群直播信息！

<br/><br/>`开启群直播模式`：开启之后会将主讲人在主讲群发送的消息转发到转发群内，支持内容格式：文字、图片、语音、表情包、文件、链接<br/>
<br/><br/>`关闭直播模式`：关闭直播模式
<br/><br/>`休眠`：所有功能关闭，只允许管理员发指令<br/>`开启`：恢复功能<br/>`退出`：退出登录
<br/><br/>

## 三、文档说明

1.[wxpy官方文档](https://wxpy.readthedocs.io/zh/latest/)

