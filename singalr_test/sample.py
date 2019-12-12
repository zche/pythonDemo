import websocket
import json
import wave
import base64

# https://github.com/aspnet/SignalR/blob/release/2.2/specs/HubProtocol.md

ws = None
#wav = b'xdf-\xde\xa7\xccA\x9b\xf1\x9a~\xd6\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9a~\x8b\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9a~\x8d\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9ay\xdc\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9a~\x88\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9ay\xda\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9ay\xd9\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9ay\x8c\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9ax\xdd\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9ax\x8d\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9a{\xda\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9a{\x8c\x9d\xdf-\xde\xa7\xccA\x9b\xf1\x9a-\xd9\x9d\xdf-\xde\xf1\x9aA\x9c\x9d\xdf-\xde\xf1\x9aA\x88\x9d\xdf-\xde\xf1\x9aA\x80\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a-\xdb\x9d\xdf-\xde\xf1\x9aA\x9a\x9d\xdf-\xde\xf1\x9aA\x9a\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a-\xd9\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a-\x8c\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a-\x88\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a,\xdc\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a,\xdb\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a,\x8f\x9d\xdf-\xde\xf1\x9aA\x9b\xf1\x9a,\x8a\x9d\xdf-\xde\xf1\x9a>\xb2\xb4\x9a-\xde\xf1\x89A\x9b\xf1\x9a-\xde\xe0\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xdf\xa5\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xdf\xf8\xf6h\xde\xf1\x9a-\xb2\xb3\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xde\xa7\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xdf\xf0\xf6h\xde\xf1\x9a-\xb2\xb5\xf6h\xde\xf1\x9a-\xb2\xa3\xf6h\xde\xf1\x9a-\xb2\xa3\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xde\xf7\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xde\xf5\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xde\xf1\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\xde\xf1\xf6h\xde\xf1\x9a-\xb2\xb4\x9a-\x88\xa7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x88\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x88\xf9\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x88\xf5\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x88\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x88\xf1\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xa3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xa0\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf9\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa5\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf5\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xa0\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf1\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf0\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf9\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf9\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf1\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8b\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xa3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xf4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xf5\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xf4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8a\xf0\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf8\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf9\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xa0\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf8\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xa5\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf8\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xa4\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xa3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xa2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf9\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf1\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8c\xa7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8c\xa7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf2\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8c\xa7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8c\xa7\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf0\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf3\xf6h\xde\xf1\xcc{\xb2\xb4\x9a-\x8d\xf9\xf6h\xde\xf1\xcc{\xcc\xed\x8a?\xbb\xb2\xcfo\xa7\xa5\x88\'\xce\xe3\x9a,\xdc\xf2\x9e(\xd8\xf6\x881\xce\xe3\xfer\x85\xa4\xc4?\xd4\xe1\x88%\xdb\x82\x9d(\xd8\xf9\xe9Y\xdf\xf4\x98(\xda\xf2\x9eX\xaf\x84\x9f-\xad\xf9\x98*\xad\x82\x99X\xd9\xf1\xe8*\xdc\xf7\x92/\xaf\xf4\x99.\xa8\xf7\x98Y\xdc\xf9\x9d)\xd7\xf2\x9c)\xaa\xf5\x99%\xdf\xf7\x9b_\xaf\x85\xee?\x93\x9c\xd7\x03'

CHUNK = 1024
# 从目录中读取语音
wf = wave.open('/Users/zhaoruifei/Study/python/singalr_test/file1.wav', 'rb')
# read data
data = wf.readframes(CHUNK)


def encode_json(obj):
    # All JSON messages must be terminated by the ASCII character 0x1E (record separator).
    # Reference: https://github.com/aspnet/SignalR/blob/release/2.2/specs/HubProtocol.md#json-encoding
    return json.dumps(obj) + chr(0x1E)

def ws_on_message(ws, message: str):
    ignore_list = ['{"type":6}', '{}']
    # Split using record seperator, as records can be received as one message
    for msg in message.split(chr(0x1E)):
        if msg and msg not in ignore_list:
            # Everything else not on ignore list
            print(f"From server: {msg}")
            # TODO: Perform your own handling here

def ws_on_error(ws, error):
    print(error)

def ws_on_close(ws):
    print("### Disconnected from SignalR Server ###")

def ws_on_open(ws):
    print("### Connected to SignalR Server via WebSocket ###")
    
    # Do a handshake request
    print("### Performing handshake request ###")
    ws.send(encode_json({
        "protocol": "json",
        "version": 1
    }))

    # Handshake completed
    print("### Handshake request completed ###")

    # Call chathub's send message method
    # Reference: https://github.com/aspnet/SignalR/blob/release/2.2/specs/HubProtocol.md#invocation-message-encoding
    ws.send(encode_json({
        "type": 1,
        "target": "VoiceStreamMessage",
        "arguments": 
        [{'BotRecordId':"f5d1d82e-a6af-48e1-b512-bf371be064be",'MessageSource':"VOIP",'VoiceStream':base64.b64encode(data).decode('ISO-8859-1'), 'UserId':"17654321",'Token':"85C7568CD1525434EAE50C827CC3E70B72682A533F62D28749364D438161BADD"}]
    }))


    print("### Hello world message sent to ChatHub ###")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://xhxzzx.eastasia.azurecontainer.io/chathub",
                              on_message = ws_on_message,
                              on_error = ws_on_error,
                              on_close = ws_on_close)
    ws.on_open = ws_on_open
    ws.run_forever()