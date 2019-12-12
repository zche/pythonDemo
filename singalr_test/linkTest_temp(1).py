
import websocket,queue,time,json
from threading import Thread
import getToken,recode # 获取token和录音的方法

# 音频队列
qt = queue.Queue(5)
# 链接
serlink ='//xhxzzx.eastasia.azurecontainer.io/chathub'

# 模拟用的音频数据
wav = b'xdf-\xde\xa7\xccA\x9b\xf1\x9a~\xd6\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9a~\x8b\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9a~\x8d\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9ay\xdc\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9a~\x88\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9ay\xda\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9ay\xd9\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9ay\x8c\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9ax\xdd\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9ax\x8d\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9a{\xda\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9a{\x8c\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9a-\xd9\x9d\xdf-\xde\xf1\x9aA\x9c\x9d\xdf-\xde\xf1\x9aA\x88\x9d\xdf-\xde\xf1\x9aA\x80\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a-\xdb\x9d\xdf-\xde\xf1\x9aA\x9a\x9d\xdf-\xde\xf1\x9aA\x9a\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a-\xd9\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a-\x8c\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a-\x88\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a,\xdc\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a,\xdb\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a,\x8f\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a,\x8a\x9d\xdf-\xde\xf1\x9a>\xb2\xb4\x9a-\xde\xf1\x89A\x9b\xf1\x9a-\xde\xe0\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xdf\xa5\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xdf\xf8\xf6h\xde\xf1\x9a-\xb2\xb3\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xde\xa7\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xdf\xf0\xf6h\xde\xf1\x9a-\xb2\xb5\xf6h\xde\xf1\x9a-\xb2\xa3\xf6h\xde\xf1\x9a-\xb2\xa3\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xde\xf7\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xde\xf5\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xde\xf1\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xde\xf1\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\x88\xa7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x88\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x88\xf9\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x88\xf5\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x88\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x88\xf1\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xa3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xa0\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf9\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa5\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf5\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xa0\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf1\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf0\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf9\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf9\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf1\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xf4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xf5\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xf4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xf0\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf8\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf9\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xa0\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf8\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xa5\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf8\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xa4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xa3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf9\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf1\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8c\xa7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8c\xa7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8c\xa7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8c\xa7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf0\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf9\xf6h\xde\xf1\xcc{\xcc\xed\x8a?\xbb\xb2\xcfo\xa7\xa5\x88\'\xce\xe3\x9a,\xdc\xf2\x9e(\xd8\xf6\x881\xce\xe3\xfer\x85\xa4\xc4?\xd4\xe1\x88%\xdb\x82\x9d(\xd8\xf9\xe9Y\xdf\xf4\x98(\xda\xf2\x9eX\xaf\x84\x9f-\xad\xf9\x98*\xad\x82\x99X\xd9\xf1\xe8*\xdc\xf7\x92/\xaf\xf4\x99.\xa8\xf7\x98Y\xdc\xf9\x9d)\xd7\xf2\x9c)\xaa\xf5\x99%\xdf\xf7\x9b_\xaf\x85\xee?\x93\x9c\xd7\x03'

# f5d1d82e-a6af-48e1-b512-bf371be064be
# 90ea68e2-479c-4bde-9e6c-3dfc22242887
datas = {
        'BotRecordId':"f5d1d82e-a6af-48e1-b512-bf371be064be",
        'hub':'chathub',
        'MessageSource':"VOIP",
        'VoiceStream':str(wav, encoding='ISO-8859-1'),
        'UserId':"01234567",
        'Token':getToken.get_token()}  # 获得token的方法


# 转json的
def encode_json(obj):
    # All JSON messages must be terminated by the ASCII character 0x1E (record separator).
    return json.dumps(obj) + chr(0x1E)

# 检查录音并发送
# def checkRecode(qtr):
#     while True:
#         if not qtr.empty():
#             print("CLINET 1 : 队列收到音频数据")
#             passtime = time.time()
#             datawav = qtr.get()
#             # 二进制编码无法转直接json
#             wav = str(datawav, encoding='ISO-8859-1')
#             datas['VoiceStream'] = wav
#             ws.send(encode_json(datas))
#             print("CLINET 2 : 获取音频数据",len(datawav))



def on_message(ws, message):
    print('get message')
    print(message)

def on_error(ws, error):
    print('error')
    print(error)

def on_open(ws):
    ws.send(encode_json({
        "protocol": "json",
        "version": 1
    }))
    time.sleep(1)
    print('send data...')
    ws.send(encode_json(datas))
    # 开启录音
    # recode.startRecode(qt)

def on_close(ws):
    print(ws)
    print("### closed ###")


websocket.enableTrace(True)
ws = websocket.WebSocketApp("ws:"+serlink,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close,
                            on_open=on_open)


# 开启录音的线程
# pt = Thread(target=checkRecode,args=(qt,))
# pt.daemon = True
# pt.start()           

print('测试开始')
ws.run_forever()