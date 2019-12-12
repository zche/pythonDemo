from pyhanlp import *
import numpy as np
import os
import sys
import time
import re

CRFLexicalAnalyzer = JClass('com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer')
sourceFile =r'/Users/zhaoruifei/Documents/sublime/宝洁修正语料/宝洁修正语料.txt' 
targetFile =r'/Users/zhaoruifei/Documents/sublime/宝洁修正语料/baojie_pos_modify.txt'

cws_path = '/Users/zhaoruifei/nlp/hanlp/myModel/cws/crf-cws-model.txt'
pos_path = '/Users/zhaoruifei/nlp/hanlp/myModel/pos/pos_all_model.txt'


def replactToNewFile(filepath):
    analyzer = CRFLexicalAnalyzer(cws_path,pos_path)
    with open(filepath, 'r+', encoding='utf-8') as f_read:
        while True:
            line = f_read.readline()
            if not line:
                break
            with open(targetFile, 'a+', encoding='utf-8') as f_write:
                str_pos = analyzer.analyze(line.lstrip('\n')).__str__()
                f_write.write(str_pos)

if __name__ == '__main__':
    print("合并文件开始时间：{timeStart}".format(timeStart=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))
    replactToNewFile(sourceFile) 
    print("合并文件结束时间：{timeEnd}".format(timeEnd=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))