from pyhanlp import *

HanLP = JClass('com.hankcs.hanlp.HanLP')
CRFSegmenter = JClass('com.hankcs.hanlp.model.crf.CRFSegmenter')
CRFLexicalAnalyzer = JClass('com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer')
CRFPOSTagger = JClass('com.hankcs.hanlp.model.crf.CRFPOSTagger')
AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')
cws_path = "/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/test/1998_cws_test/tv-cws-model.txt"


def load_model():
    present_model_path = "/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/test/1998_pos_test/tv_pos.bin"
    # present_model_path = "/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/test/1998_pos_test/pos.bin.txt"
    # present_model_path = "/Users/zhaoruifei/git/NLP/HanLP/external/data/model/crf/pku199801/pos.txt.bin"
    seg = CRFSegmenter(cws_path)
    tagger = CRFPOSTagger(present_model_path)
    analyzer = CRFLexicalAnalyzer(cws_path,present_model_path)
    # analyzer = AbstractLexicalAnalyzer(seg,tagger)
    # analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(), tagger)  # 构造词法分析器
    str1 = "李狗蛋的希望是希望上学"
    str1 ="小米全面屏电视E65A65英寸4K超高清HDR内置小爱蓝牙语音2GB8GBAI人工智能网络液晶平板电视L65M5-EA现在点击预约，零点开抢到手价只要2699元，速速排队吧"
    str1 = '''
    '''
    result = analyzer.analyze(str1).__str__()
    print(result)  # 分词+词性标注
    # wordList = seg.segment(str1)
    # print(wordList)
    # print(','.join(tagger.tag(wordList)))
    # print(analyzer.neRecognizer.recognize(str1))
    # print(analyzer.neRecognizer.getNERTagSet(str1))
    return tagger

def train_model():
    origin_model_path = "/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/test/1998_pos_test/pos.bin.txt"
    # tagger = CRFPOSTagger(origin_model_path) # 加载
    tagger = CRFPOSTagger(None) 
    # train_file = "/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/test/1998_pos_test/tv-train.txt"
    # present_model_path = "/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/test/1998_pos_test/tv_pos.bin"
    
    # train_file = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/corpus/pos_baojie.txt'
    # present_model_path =  '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/model/baj-pos-model'
    train_file = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/tmp/corpus/pos_baojie.txt'
    present_model_path =  '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/tmp/model/baj-pos-model'
    tagger.train(train_file, present_model_path)  # 训练

    
    # tagger = CRFPOSTagger(present_model_path) # 加
    # 选项2.使用CRF++训练，HanLP加载。（训练命令由选项1给出）
    # tagger = CRFPOSTagger(POS_MODEL + ".txt")
    # print(', '.join(tagger.tag("他", "的", "希望", "是", "希望", "上学")))  # 预测
    # cws_path = "/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/test/1998_cws_test/tv-cws-model"
    # analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(cws_path), tagger)  # 构造词法分析器
    # cws_path = "/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/test/1998_cws_test/tv-cws-model.txt"
    cws_path = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/tmp/model/baj-cws-model.txt'
    analyzer = CRFLexicalAnalyzer(cws_path,present_model_path+".txt")
    str1 = "李狗蛋的希望是希望上学"
    str1 ="小米全面屏电视E65A65英寸4K超高清HDR内置小爱蓝牙语音2GB8GBAI人工智能网络液晶平板电视L65M5-EA现在点击预约，零点开抢到手价只要2699元，速速排队吧"
    str1 = '潘婷氨基酸洗护套装乳液修护洗发水500ml搭配3分钟奇迹护发素70ml 新旧包装随机发货，价格￥59.90，适合头皮：干性，功效：水润。'

    print(analyzer.analyze(str1))  # 分词+词性标注
    # print(analyzer.seg(str1))
    return tagger

if __name__ == '__main__':
    # tagger = train_crf_pos(PKU199801_TRAIN)
    # model_path = "/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/test/1998_pos_test/pos.bin.txt"
    # load_crf_pos(model_path)
    # load_model()
    train_model()
    # print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))