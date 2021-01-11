# -*- coding: utf-8 -*-
import os
import time
import threading
import ali_speech
from ali_speech.callbacks import SpeechTranscriberCallback
from ali_speech.constant import ASRFormat
from ali_speech.constant import ASRSampleRate

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json



class MyCallback(SpeechTranscriberCallback):
    """
    构造函数的参数没有要求，可根据需要设置添加
    示例中的name参数可作为待识别的音频文件名，用于在多线程中进行区分
    """
    def __init__(self, name='default'):
        self._name = name
    def on_started(self, message):
        print('MyCallback.OnRecognitionStarted: %s' % message)
    def on_result_changed(self, message):
        print('MyCallback.OnRecognitionResultChanged: file: %s, task_id: %s, result: %s' % (
            self._name, message['header']['task_id'], message['payload']['result']))
    def on_sentence_begin(self, message):
        print('MyCallback.on_sentence_begin: file: %s, task_id: %s, sentence_id: %s, time: %s' % (
            self._name, message['header']['task_id'], message['payload']['index'], message['payload']['time']))
    def on_sentence_end(self, message):
        print('MyCallback.on_sentence_end: file: %s, task_id: %s, sentence_id: %s, time: %s, result: %s' % (
            self._name,
            message['header']['task_id'], message['payload']['index'],
            message['payload']['time'], message['payload']['result']))
    def on_completed(self, message):
        print('MyCallback.OnRecognitionCompleted: %s' % message)
    def on_task_failed(self, message):
        print('MyCallback.OnRecognitionTaskFailed-task_id:%s, status_text:%s' % (
            message['header']['task_id'], message['header']['status_text']))
    def on_channel_closed(self):
        print('MyCallback.OnRecognitionChannelClosed')
def process(client, appkey, token):
    audio_name = '/Users/zhaoruifei/Study/python/speechRecognize/aliyun/conversationRecord.wav'
    callback = MyCallback(audio_name)
    transcriber = client.create_transcriber(callback)
    # transcriber.set_url("wss://nls-gateway-ap-southeast-1.aliyuncs.com/ws/v1")
    transcriber.set_appkey(appkey)
    transcriber.set_token(token)
    transcriber.set_format(ASRFormat.PCM)
    transcriber.set_sample_rate(ASRSampleRate.SAMPLE_RATE_8K)
    transcriber.set_enable_intermediate_result(False)
    transcriber.set_enable_punctuation_prediction(True)
    transcriber.set_enable_inverse_text_normalization(True)
    try:
        ret = transcriber.start()
        if ret < 0:
            return ret
        print('sending audio...')
        with open(audio_name, 'rb') as f:
            audio = f.read(3200)
            while audio:
                ret = transcriber.send(audio)
                if ret < 0:
                    break
                time.sleep(0.1)
                audio = f.read(3200)
        transcriber.stop()
    except Exception as e:
        print(e)
    finally:
        transcriber.close()
def process_multithread(client, appkey, token, number):
    thread_list = []
    for i in range(0, number):
        thread = threading.Thread(target=process, args=(client, appkey, token))
        thread_list.append(thread)
        thread.start()
    for thread in thread_list:
        thread.join()
if __name__ == "__main__":
    # 创建AcsClient实例
    client = AcsClient(
    "LTAI4GKBS1ExNhnjqdh6pGhQ",
    "JBraHsGCr6CHWevkHuhlU3jY65hcPV",
    "cn-shanghai"
    );

    # 创建request，并设置参数。
    request = CommonRequest()
    request.set_method('POST')
    request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
    request.set_version('2019-02-28')
    request.set_action_name('CreateToken')
    response = bytes.decode(client.do_action_with_exception(request))
    print("==================================================")
    print(response)
    respJson = json.loads(response)
    print(respJson)
    # print(bytes.decode(response))
    client = ali_speech.NlsClient()
    # 设置输出日志信息的级别：DEBUG、INFO、WARNING、ERROR
    client.set_log_level('INFO')
    appkey = 'B58u85dnZs5cirr1'
    token = respJson['Token']['Id']
    process(client, appkey, token)
    print("end")
    # 多线程示例
    # process_multithread(client, appkey, token, 2)