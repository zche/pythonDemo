from pyhanlp import *
import os


POSTrainer = JClass('com.hankcs.hanlp.model.perceptron.POSTrainer')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')
AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')

cws_model = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/model/perceptron/cws.bin'
pos_model = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/model/perceptron/pos.bin'

def train_perceptron_pos(corpus):
    trainer = POSTrainer()
    trainer.train(corpus, pos_model) 
    tagger = PerceptronPOSTagger(pos_model)
    analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(cws_model), tagger)  # 构造词法分析器
    sent = '潘婷氨基酸洗护套装乳液修护洗发水500ml搭配3分钟奇迹护发素70ml 新旧包装随机发货，价格￥59.90，适合头皮：干性，功效：水润。'
    print(analyzer.analyze(sent)) 
    return tagger

def load():
    model_cws = PerceptronSegmenter(cws_model)
    sent = '潘婷氨基酸洗护套装乳液修护洗发水500ml搭配3分钟奇迹护发素70ml 新旧包装随机发货，价格￥59.90，适合头皮：干性，功效：水润。'
    tokens = model_cws.segment(sent)
    model_pos = PerceptronPOSTagger(pos_model)
    print(model_pos.tag(tokens))
    return model_pos


if __name__ == '__main__':
    # train_file = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/corpus/pos_baojie.txt'
    # train_perceptron_pos(train_file)
    load()