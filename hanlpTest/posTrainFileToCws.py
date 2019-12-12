import io
import os
import re
import time

WORK_PATH = r'/Users/zhaoruifei/Study/python/People_Daily_1998_01_06'
sourceFile =r'/Users/zhaoruifei/Study/python/People_Daily_1998_01_06/merge1998.txt' 
targetFile =r'/Users/zhaoruifei/Study/python/People_Daily_1998_01_06/cwsMerge1998.txt'

sourceFile =r'/Users/zhaoruifei/Documents/sublime/pos_baojie1.txt' 
targetFile =r'/Users/zhaoruifei/Documents/sublime/cws_baojie1.txt'

sourceFile =r'/Users/zhaoruifei/Documents/sublime/宝洁修正语料/baojie_pos_modify.txt'
targetFile =r'/Users/zhaoruifei/Documents/sublime/宝洁修正语料/baojie_cws_modify.txt'


def replactToNewFile(filepath):
    with open(filepath, 'r+', encoding='utf-8') as f_read:
        while True:
            line = f_read.readline()
            if not line:
                break
            with open(targetFile, 'a+', encoding='utf-8') as f_write:
                str2 = re.sub('/[a-zA-Z]+', '', line)
                str3 = re.sub('[\[\]]','',str2)
                f_write.write(str3)

if __name__ == '__main__':
    print("合并文件开始时间：{timeStart}".format(timeStart=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))
    replactToNewFile(sourceFile) 
    print("合并文件结束时间：{timeEnd}".format(timeEnd=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))