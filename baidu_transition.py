# 百度转换
from aip import AipSpeech
from io import BytesIO
from pydub import AudioSegment


"""百度语音申请地址：http://yuyin.baidu.com/"""
APP_ID = '16031816'
API_KEY = 'mwK1Oul70bWZLXvx5EwSNK2A'
SECRET_KEY = 'ZBR34U4aaWNjl83TUkkcGliKDzZYMoSa'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def voice_to_text(msg):
    """语言转文字"""
    response = client.asr(get_file_content(msg), 'amr', 8000, {
        'dev_pid': 1537,
    })
    if response and response['err_no'] == 0:
        return response['result'][0]
    return None


def get_file_content(msg):
    """读取文件"""
    audio = AudioSegment.from_mp3(BytesIO(msg.get_file()))
    export = audio.export(format="amr", bitrate="12.20k")
    return export.read()


if __name__ == '__main__':
    """测试百度转换接口"""
    file_io = None
    with open('baidu-test.m4a', 'rb') as fp:
        file_io = fp.read()
    response_json = client.asr(file_io, 'm4a', 16000, {
        'dev_pid': 1537,
    })
    print(response_json['result'][0])




