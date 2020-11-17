import io
import os
import numpy as np
import time

originFile = r'/Users/zhaoruifei/Study/python/files/chineseTxts/chars.txt'
targetFile =r'/Users/zhaoruifei/Study/python/files/chineseTxts/all_chinese_chars.txt' 

print("合并文件开始时间：{timeStart}".format(timeStart=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))
with open(targetFile, 'a+', encoding='utf-8') as f_write:
    with open(originFile, 'r+', encoding='utf-8') as f_read:
        while True:
            line = f_read.readline()
            if not line:
                break
            arr = line.split("\"")
            f_write.write(arr[1])
print("合并文件结束时间：{timeEnd}".format(timeEnd=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))