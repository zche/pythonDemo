from  pyhanlp import *
import os

AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')

cws_path = '/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/model/perceptron/pku1998/cws.bin'
cws_path = '/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/model/perceptron/large/cws.bin'
pos_path = '/Applications/anaconda3/lib/python3.7/site-packages/pyhanlp-0.1.57-py3.7.egg/pyhanlp/static/data/model/perceptron/pku1998/pos.bin'

cws_model = PerceptronSegmenter(cws_path)
pos_model = PerceptronPOSTagger(pos_path) 

analyzer = AbstractLexicalAnalyzer(cws_model, pos_model)  # 包装
str2 = '潘婷氨基酸护发素3分钟奇迹烫染修护180ml 三分钟 护色 滋养 防枯黄，价格￥38.90，适合头皮：干性，功效：柔顺。'
str2 = '这三个品牌都属于宝洁公司的品牌，在洗发露方面各自有优势：'
sentence = analyzer.analyze(str2)
# for word in sentence.wordList:
#     print('{}\t{}'.format(word.getValue(), word.getLabel())) # 获取单词与词性
print(sentence)  # 