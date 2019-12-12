from pyhanlp import *
import os

NERTrainer = JClass('com.hankcs.hanlp.model.perceptron.NERTrainer')
PerceptronNERecognizer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronNERecognizer')
CWSTrainer = JClass('com.hankcs.hanlp.model.perceptron.CWSTrainer')
POSTrainer = JClass('com.hankcs.hanlp.model.perceptron.POSTrainer')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')
AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')


train_file = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/tmp/corpus/pos_baojie.txt'
train_file = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/corpus/pos_baojie.txt'
ner_model = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/model/perceptron/ner.bin'
cws_model = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/model/perceptron/cws.bin'
pos_model = '/Users/zhaoruifei/Work/Pactera/NLP/宝洁项目/model/perceptron/pos.bin'

def train_ner():
        trainer = NERTrainer()
        trainer.tagSet.nerLabels.clear()  
        trainer.tagSet.nerLabels.add("baj") 
        trainer.tagSet.nerLabels.add("price") 
        trainer.tagSet.nerLabels.add("rong")  
        recognizer = PerceptronNERecognizer(trainer.train(train_file, ner_model).getModel())
        analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(cws_model), PerceptronPOSTagger(pos_model), recognizer)
        sent = '潘婷氨基酸洗护套装乳液修护洗发水500ml搭配3分钟奇迹护发素70ml 新旧包装随机发货，价格￥59.90，适合头皮：干性，功效：水润。'
        print(analyzer.analyze(sent))

def load_ner():
        model_ner = PerceptronNERecognizer(ner_model)
        model_ner.getNERTagSet().nerLabels.add('baj')
        model_ner.getNERTagSet().nerLabels.add('price')
        model_ner.getNERTagSet().nerLabels.add('rong')
        tagSets = list(model_ner.getNERTagSet().nerLabels)
        print(tagSets)

        model_cws = PerceptronSegmenter(cws_model)
        sent = '潘婷氨基酸洗护套装乳液修护洗发水500ml搭配3分钟奇迹护发素70ml 新旧包装随机发货，价格￥59.90，适合头皮：干性，功效：水润。'
        # sent = '潘婷深水泡弹沁润水养洗发水530ml搭配保湿双萃护发素200ml-滋养型（修护补水 长效保湿）送旅行装洗发水50ml*2，价格￥179.00，商品名称：潘婷洗护发用品，功效：滋润。'
        # sent = '飘柔香氛洗发水甜美花漾2530ml（花香调滋润柔滑 持久留香 新老包装随机发货）王俊凯同款，价格￥37.80，适合头皮：干性，功效：滋润。'
        # sent = '潘婷氨基酸洗护套装乳液修护洗发水750ml 秀发能量水 新老包装随机发送，价格￥79.80，商品毛重：0.84kg，商品产地：杭州，适合头皮：干性，功效：修护，净含量：401-750mL，适用人群：通用，适合发质：受损(染烫1-2次)。'
        # sent = '功效：修护，净含量：4031-75220mL，适用人群：通用，适合发质：受损(染烫1-2次)。'
        sent = '潘婷氨基酸洗护套装乳液修护洗发水500ml搭配3分钟奇迹护发素70ml 新旧包装随机发货，价格￥59.90，适合头皮：干性，功效：水润>。'
        tokens = model_cws.segment(sent)
        print(len(tokens))
        model_pos = PerceptronPOSTagger(pos_model)
        pos_tags = model_pos.tag(tokens)
        print(len(pos_tags))
        ner_tags = list(model_ner.recognize(list(tokens),list(pos_tags)))
        print(len(ner_tags))
        print(ner_tags)

        # trainer = NERTrainer()
        # trainer.tagSet.nerLabels.clear()  
        # trainer.tagSet.nerLabels.add("baj") 
        # analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(cws_model), PerceptronPOSTagger(pos_model), PerceptronNERecognizer(ner_model))
        # sent = '潘婷氨基酸洗护套装乳液修护洗发水500ml搭配3分钟奇迹护发素70ml 新旧包装随机发货，价格￥59.90，适合头皮：干性，功效：水润。'
        # print(analyzer.analyze(sent))

if __name__ == '__main__':
#     train_ner()
    load_ner()