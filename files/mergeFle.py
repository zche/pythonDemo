import io
import os
import numpy as np
import time

# WORK_PATH = r'/Users/zhaoruifei/Study/python/People_Daily_1998_01_06'
# targetFile =r'/Users/zhaoruifei/Study/python/People_Daily_1998_01_06/merge1998.txt' 
WORK_PATH = r'/Users/zhaoruifei/git/NLP/spellCheck/JamSpell/test_data/caijing'
targetFile =r'/Users/zhaoruifei/Study/python/files/mergeChineseTxts.txt' 

def getFiles():
    filepaths = []
    if os.access(path=WORK_PATH, mode=os.R_OK):
        for flieName in os.listdir(WORK_PATH):
            filepaths.append(r'{0}/{1}'.format(WORK_PATH, flieName))
        return filepaths
    else:
        raise Exception("文件不可读或者文件不存在")

def mergeNewFile(filepath):
    with open(targetFile, 'a+', encoding='utf-8') as f_write:
        with open(filepath, 'r+', encoding='utf-8') as f_read:
            while True:
                line = f_read.readline()
                if not line:
                    break
                f_write.write(line)
        # f_write.write("\n\n")
                
                    

if __name__ == '__main__':
    print("合并文件开始时间：{timeStart}".format(timeStart=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))
    filepaths = getFiles()
    for filepath in filepaths:
        mergeNewFile(filepath)
    print("合并文件结束时间：{timeEnd}".format(timeEnd=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))