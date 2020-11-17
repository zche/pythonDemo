import io
import os
import numpy as np
import time
import re

originFile = r'/Users/zhaoruifei/Downloads/hanzi-convert-master/src/hanziDict.txt'
simpleFile = r'/Users/zhaoruifei/Downloads/hanzi-convert-master/src/hanziDict_simple.txt'
traditionalFile = r'/Users/zhaoruifei/Downloads/hanzi-convert-master/src/hanziDict_traditonal.txt'

simpleArray = []
traditionalArray = []

print("合并文件开始时间：{timeStart}".format(timeStart=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))
with open(originFile, 'r+', encoding='utf-8') as f_read:
    while True:
        line = f_read.readline()
        if not line:
            break
        arr = line.split("'")
        if re.match(u'^[\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ff]+$', str(arr[3])) == None:
            continue
        if arr[3] not in simpleFile:
            simpleArray.append(arr[3])
        if arr[1] not in traditionalArray:
            traditionalArray.append(arr[1])

with open(simpleFile, 'a+', encoding='utf-8') as f_write:
    f_write.write(''.join(simpleArray))
with open(traditionalFile, 'a+', encoding='utf-8') as f_write:
    f_write.write(''.join(traditionalArray))
print("合并文件结束时间：{timeEnd}".format(timeEnd=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))