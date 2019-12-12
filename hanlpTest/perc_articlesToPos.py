from pyhanlp import *
import numpy as np
import os
import sys
import time
import re

AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')

cws_path = '/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/model/perceptron/pku1998/cws.bin'
cws_path = '/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/model/perceptron/large/cws.bin'
pos_path = '/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/model/perceptron/pku1998/pos.bin'

sourceFile =r'/Users/zhaoruifei/Documents/sublime/baojie_corpus.txt' 
targetFile =r'/Users/zhaoruifei/Documents/sublime/pos_baojie.txt'

cws_model = PerceptronSegmenter(cws_path)
pos_model = PerceptronPOSTagger(pos_path) 


def replactToNewFile(filepath):
    analyzer = AbstractLexicalAnalyzer(cws_model, pos_model)
    with open(filepath, 'r+', encoding='utf-8') as f_read:
        while True:
            line = f_read.readline()
            if not line:
                break
            with open(targetFile, 'a+', encoding='utf-8') as f_write:
                str_pos = analyzer.analyze(line.lstrip('\n').rstrip('\n')).__str__()
                f_write.write(str_pos)
                f_write.write('\n')

if __name__ == '__main__':
    print("合并文件开始时间：{timeStart}".format(timeStart=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))
    replactToNewFile(sourceFile) 
    print("合并文件结束时间：{timeEnd}".format(timeEnd=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))