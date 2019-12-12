from pyhanlp import *
import numpy as np
import os
import sys
import time
import re


sourceFile =r'/Users/zhaoruifei/Documents/sublime/宝洁修正语料/宝洁修正语料.txt' 
targetFile =r'/Users/zhaoruifei/Documents/sublime/宝洁修正语料/baojie_pos_modify.txt'
# sourceFile =r'/Users/zhaoruifei/Documents/sublime/baojie_corpus.txt' 
# targetFile =r'/Users/zhaoruifei/Documents/sublime/pos_baojie1.txt'



def replactToNewFile(filepath):
    with open(filepath, 'r+', encoding='utf-8') as f_read:
        while True:
            line = f_read.readline()
            if not line:
                break
            with open(targetFile, 'a+', encoding='utf-8') as f_write:
                str_pos = HanLP.segment(line.lstrip('\n').rstrip('\n')).__str__().replace(',','')[1:-1]
                f_write.write(str_pos+'\n')

if __name__ == '__main__':
    print("转换文件开始时间：{timeStart}".format(timeStart=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))
    replactToNewFile(sourceFile) 
    print("转换文件结束时间：{timeEnd}".format(timeEnd=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))