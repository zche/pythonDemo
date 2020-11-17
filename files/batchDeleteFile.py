import io
import os
import numpy as np
import time

WORK_PATH = r'/Users/zhaoruifei/Life/赵锐飞'
targetFile =r'/Users/zhaoruifei/Study/python/files/mergeChineseTxts.txt' 

def getFiles():
    filepaths = []
    if os.access(path=WORK_PATH, mode=os.R_OK):
        for flieName in os.listdir(WORK_PATH):
            filepaths.append(r'{0}/{1}'.format(WORK_PATH, flieName))
        return filepaths
    else:
        raise Exception("文件不可读或者文件不存在")


if __name__ == '__main__':
    print("删除文件开始时间：{timeStart}".format(timeStart=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))
    filepaths = getFiles()
    for filepath in filepaths:
        if "(2)" in filepath:
            os.remove(filepath)
    print("删除文件结束时间：{timeEnd}".format(timeEnd=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))