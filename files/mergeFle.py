import io
import os
import numpy as np
import time

# WORK_PATH = r'/Users/zhaoruifei/Study/python/People_Daily_1998_01_06'
# targetFile =r'/Users/zhaoruifei/Study/python/People_Daily_1998_01_06/merge1998.txt' 
WORK_PATH = r'/Users/zhaoruifei/git/NLP/spellCheck/JamSpell/test_data/test1'
targetFile =r'/Users/zhaoruifei/Study/python/files/mergeChineseTxts_new_itr.txt' 

filepaths = []

def getFiles():
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

def readAllFiles(workPath):
  files = os.listdir(workPath)
  for fi in files:
    fi_d = os.path.join(workPath,fi)            
    if os.path.isdir(fi_d):
      readAllFiles(fi_d)                  
    else:
        filepaths.append(fi_d)
  return filepaths
                
                    

if __name__ == '__main__':
    print("合并文件开始时间：{timeStart}".format(timeStart=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))
    filepaths = readAllFiles(WORK_PATH)
    # filepaths = getFiles()
    # for filepath in filepaths:
    #     mergeNewFile(filepath)
    with open(targetFile, 'a+', encoding='utf-8') as f_write:
        for filepath in filepaths:
            if os.path.splitext(filepath)[1] == '.txt':
                with open(filepath, 'r+', encoding='utf-8') as f_read:
                    while True:
                        line = f_read.readline()
                        if not line:
                            break
                        f_write.write(line)
    print("合并文件结束时间：{timeEnd}".format(timeEnd=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))