from pyhanlp import *
import os

CRFLexicalAnalyzer = JClass('com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer')
CRFSegmenter = JClass('com.hankcs.hanlp.model.crf.CRFSegmenter')
base_path = "/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/test/1998_cws_test"
origin_model_path = os.path.join(base_path,"crf-cws-model.txt") 

def cws_load():
    origin_model_path = "/Users/zhaoruifei/git/NLP/HanLP/external/data/model/crf/pku199801/cws.txt.bin"
    origin_model_path = os.path.join(base_path,"tv-cws-model.txt")
    # segmenter = CRFLexicalAnalyzer(origin_model_path)
    # segmenter = CRFSegmenter(origin_model_path)
    segmenter = CRFLexicalAnalyzer(origin_model_path)
    return segmenter

def train_load():
    segmenter = CRFSegmenter(None)
    trainfile = os.path.join(base_path,"tv-train.utf8")
    final_path = os.path.join(base_path,"tv-cws-model")
    # trainfile = '/Users/zhaoruifei/Study/python/People_Daily_1998_01_06/cwsMerge1998.txt'
    # trainfile = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/corpus/cws_baojie.txt'
    # final_path =  '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/model/baj-cws-model'
    trainfile = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/tmp/corpus/cws_baojie.txt'
    final_path =  '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/tmp/model/baj-cws-model'
    segmenter.train(trainfile,final_path)
    seg_model = CRFLexicalAnalyzer(final_path+".txt")
    print(final_path)
    return seg_model


if __name__ == '__main__':
    # segment = cws_load()
    segment = train_load()
    str1 = "商品和服务"
    str1 = "李狗蛋的希望是希望上学"
    str1 = "小米全面屏电视E65A65英寸 4K超高清 HDR 内置小爱 蓝牙语音 2GB8GB AI人工智能网络液晶平板电视L65M5-EA现在点击预约，零点开抢到手价只要2699元，速速排队吧"
    str1 = '潘婷氨基酸洗护套装乳液修护洗发水500ml搭配3分钟奇迹护发素70ml 新旧包装随机发货，价格￥59.90，适合头皮：干性，功效：水润。'
    # str1 = "功能方面，索尼KD-49X8000G液晶电视搭载了安卓7.0系统，能让用户轻松享受大量不同类型的APP内容"
    # print(segment.segment(str1))
    print(segment.analyze(str1))
