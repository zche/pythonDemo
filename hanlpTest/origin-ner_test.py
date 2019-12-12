from pyhanlp import *
import os

NERTrainer = JClass('com.hankcs.hanlp.model.perceptron.NERTrainer')
CRFNERecognizer = JClass('com.hankcs.hanlp.model.crf.CRFNERecognizer')
CRFSegmenter = JClass('com.hankcs.hanlp.model.crf.CRFSegmenter')
CRFLexicalAnalyzer = JClass('com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer')
CRFPOSTagger = JClass('com.hankcs.hanlp.model.crf.CRFPOSTagger')
AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')

str1 = '在１９９８年来临之际，我十分高兴地通过中央人民广播电台、中国国际广播电台和中央电视台，向全国各族人民，向香港特别行政区同胞、澳门和台湾同胞、海外侨胞，向世界各国的朋友们，致以诚挚的问候和良好的祝愿！'
seg = CRFSegmenter()
wordList = seg.segment(str1)
tagger = CRFPOSTagger()
pos_tags = tagger.tag(wordList)
ner = CRFNERecognizer()
arrNer = ner.recognize(list(wordList),list(pos_tags))
ner_tags = list([p for p in list(arrNer)])
print(ner_tags)