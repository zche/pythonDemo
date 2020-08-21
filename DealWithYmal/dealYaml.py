import yaml
import os

path = os.getcwd()
print(path)

with open("/Users/zhaoruifei/Study/python/DealWithYmal/config_embedding_bert_intent_estimator_classifier.yml", "r") as yaml_file:
    yaml_obj = yaml.load(yaml_file.read())
    # intent_classifier = yaml_obj['pipeline'][2]
    # if 'intent_split_symbol' in intent_classifier: 
    #     print(intent_classifier['intent_split_symbol'])

# 写入 yaml 文件
with open("/Users/zhaoruifei/Study/python/DealWithYmal/config_embedding_bert_intent_estimator_classifier.yml", "w") as yaml_file:
    yaml_obj['pipeline'][2]['intent_split_symbol']='_'
    yaml.dump(yaml_obj, yaml_file)
