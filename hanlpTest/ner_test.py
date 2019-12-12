from pyhanlp import *
import os

NERTrainer = JClass('com.hankcs.hanlp.model.perceptron.NERTrainer')
CRFNERecognizer = JClass('com.hankcs.hanlp.model.crf.CRFNERecognizer')
CRFSegmenter = JClass('com.hankcs.hanlp.model.crf.CRFSegmenter')
CRFLexicalAnalyzer = JClass('com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer')
CRFPOSTagger = JClass('com.hankcs.hanlp.model.crf.CRFPOSTagger')
AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')

# cws_path = "/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/test/1998_cws_test/tv-cws-model.txt"
# pos_path = "/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/test/1998_pos_test/tv_pos.bin"
# base_path = "/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/test/1998_ner_test"
# train_file = os.path.join(base_path,"tv-train.txt")
# train_model = os.path.join(base_path,"tv-model.bin")

# train_file = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/corpus/pos_baojie.txt'
# train_model =  '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/model/baj-ner-model'

# cws_path = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/model/baj-cws-model.txt'
# pos_path = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/model/baj-pos-model.txt'

train_file = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/tmp/corpus/pos_baojie.txt'
train_model =  '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/tmp/model/baj-ner-model'

cws_path = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/tmp/model/baj-cws-model.txt'
pos_path = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/tmp/model/baj-pos-model.txt'
# train_model =  '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/tmp/model/baj-ner-model.txt'

def train(corpus, model):
    recognizer = CRFNERecognizer(None)  
    recognizer.getNERTagSet().nerLabels.clear()
    recognizer.getNERTagSet().nerLabels.add("baj")
    recognizer.train(corpus, model)
    # seg = CRFSegmenter(cws_path)
    # tagger = CRFPOSTagger(pos_path)
    # # ner = CRFNERecognizer(train_model)
    # analyzer = AbstractLexicalAnalyzer(seg, tagger, recognizer)
    # print(analyzer.analyze("小米全面屏电视E65A65英寸4K超高清HDR内置小爱蓝牙语音2GB8GBAI人工智能网络液晶平板电视L65M5-EA现在点击预约，零点开抢到手价只要2699元，速速排队吧"))
    return recognizer
def test():
    str1 = '潘婷氨基酸洗护套装乳液修护洗发水500ml搭配3分钟奇迹护发素70ml新旧包装随机发货，价格￥59.90，适合头皮：干性，功效：水润。'
    seg = CRFSegmenter(cws_path)
    wordList = seg.segment(str1)
    tagger = CRFPOSTagger(pos_path)
    pos_tags = tagger.tag(wordList)
    customNerTags = ['baj']
    ner = CRFNERecognizer(train_model+".txt",customNerTags)
    arrNer = ner.recognize(list(wordList),list(pos_tags))
    ner_tags = list([p for p in list(arrNer)])
    print(ner_tags)
    # analyzer = AbstractLexicalAnalyzer(seg, tagger, ner)

    analyzer = AbstractLexicalAnalyzer(seg, CRFPOSTagger(), ner)
    str1 = '小米全面屏电视E65A65英寸4K超高清HDR内置小爱蓝牙语音2GB8GBAI人工智能网络液晶平板电视L65M5-EA现在点击预约，零点开抢到手价只要2699元，速速排队吧'
    str1 = '潘婷氨基酸洗护套装乳液修护洗发水500ml搭配3分钟奇迹护发素70ml 新旧包装随机发货，价格￥59.90，适合头皮：干性，功效：水润。'

    # str1 = '潘婷氨基酸洗护套装乳液修护洗发水500ml搭配3分钟奇迹护发素70ml '
    # print(analyzer.analyze(str1))

if __name__ == '__main__':
    # recognizer = train(train_file, train_model)
    test()
