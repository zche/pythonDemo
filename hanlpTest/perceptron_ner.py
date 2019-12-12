from  pyhanlp import *


NERTrainer = JClass('com.hankcs.hanlp.model.perceptron.NERTrainer')
PerceptronNERecognizer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronNERecognizer')
AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')

PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')

cws_path = '/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/model/perceptron/pku1998/cws.bin'
cws_path = '/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/model/perceptron/large/cws.bin'
pos_path = '/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/model/perceptron/pku1998/pos.bin'

cws_model = PerceptronSegmenter(cws_path)
pos_model = PerceptronPOSTagger(pos_path) 

ner_trainFile = '/Users/zhaoruifei/Documents/sublime/pos_baojie.txt'
ner_model_path = '/Users/zhaoruifei/Documents/sublime/ner_baojie.bin'

ner_trainFile = '/Users/zhaoruifei/Study/python/People_Daily_1998_01_06/merge1998.txt'
ner_model_path = '/Users/zhaoruifei/Study/python/People_Daily_1998_01_06/ner_baojie.bin'


if __name__ == '__main__':
    trainer = NERTrainer()
    trainer.tagSet.nerLabels.clear()  # 不识别nr、ns、nt
    trainer.tagSet.nerLabels.add("baj")  # 目标是识别np
    recognizer = PerceptronNERecognizer(trainer.train(ner_trainFile, ner_model_path).getModel())
    analyzer = AbstractLexicalAnalyzer(cws_model, pos_model, recognizer)
    str1 ='潘婷氨基酸洗护套装乳液修护洗发水500ml搭配3分钟奇迹护发素70ml 新旧包装随机发货，价格￥59.90，适合头皮：干性，功效：水润。'
    print(analyzer.analyze(str1))