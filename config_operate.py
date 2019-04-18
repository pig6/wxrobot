from configparser import ConfigParser


# 初始化类和配置块
__cp = ConfigParser()
__cp.read("common.cfg")
__tuling_section = __cp.sections()[0]
__baidu_section = __cp.sections()[1]

# 图灵机器人配置
tuling_api_key = __cp.get(__tuling_section, 'tuling_api_key')


# 百度语音配置
baidu_yuyin_app_id = __cp.get(__baidu_section, 'baidu_yuyin_app_id')
baidu_yuyin_api_key = __cp.get(__baidu_section, 'baidu_yuyin_api_key')
baidu_yuyin_secret_key = __cp.get(__baidu_section, 'baidu_yuyin_secret_key')





