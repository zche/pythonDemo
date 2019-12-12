from pyhanlp import *
import os

CWSTrainer = JClass('com.hankcs.hanlp.model.perceptron.CWSTrainer')
PerceptronLexicalAnalyzer = SafeJClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')

train_file = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/corpus/cws_baojie.txt'
cws_model = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/model/perceptron/cws.bin'

def train():
    model = CWSTrainer().train(train_file, cws_model).getModel()  # 训练模型
    segment = PerceptronLexicalAnalyzer(model).enableCustomDictionary(False)  # 创建分词器
    sent = '潘婷氨基酸洗护套装乳液修护洗发水500ml搭配3分钟奇迹护发素70ml 新旧包装随机发货，价格￥59.90，适合头皮：干性，功效：水润。'
    print(segment.seg(sent))
    return segment
    # print(CWSEvaluator.evaluate(segment, msr_test, msr_output, msr_gold, msr_dict))  # 标准化评测
def load():
    model = PerceptronSegmenter(cws_model)
    sent = '潘婷氨基酸洗护套装乳液修护洗发水500ml搭配3分钟奇迹护发素70ml 新旧包装随机发货，价格￥59.90，适合头皮：干性，功效：水润。'
    print(model.segment(sent))
    return model

if __name__ == '__main__':
    # segment = train()
    segment = load()
