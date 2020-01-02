import io
import os
import json
import numpy as np

WORK_PATH = r'/Users/zhaoruifei/Work/Pactera/NLP/培训数据/徐汇行政中心/v0.6test'
TARGET_PATH = r'/Users/zhaoruifei/Work/Pactera/NLP/培训数据/徐汇行政中心/shufffleJson'

intents = []
closedLists = []
utterances = []


def lookupdir():
    filepaths = []
    os.access(path=WORK_PATH, mode=os.R_OK)
    for flieName in os.listdir(WORK_PATH):
        filepaths.append(r'{0}/{1}'.format(WORK_PATH, flieName))
    return filepaths


def readfile(filepath):
    with open(filepath, 'r+', encoding='utf-8') as f:
        jsonInfo = json.loads(f.read())
        # intents.append(jsonInfo["intents"])
        # closedLists.append(jsonInfo["closedLists"])
        # utterances.append(jsonInfo["utterances"])
        for item in jsonInfo["intents"]: intents.append(item) 
        for item in jsonInfo["closedLists"]: closedLists.append(item)
        for item in jsonInfo["utterances"]: utterances.append(item) 
        

def writeinrasafile():
    rasadata={
    "rasa_nlu_data": {
       "regex_features": [],
       "entity_synonyms": [],
       "common_examples":utterances
    }
    }
    json_str_rasa = json.dumps(rasadata,indent=2, ensure_ascii=False)
    with open("{0}/merge-rasa.json".format(TARGET_PATH), "w",encoding='utf-8') as f:
        f.write(json_str_rasa)

def writeluisinfile():
    np.random.shuffle(utterances)
    np.random.shuffle(intents)
    luisdata={
    "luis_schema_version":"2.2.0",
    "versionId": "0.6",
    "name": "xiaohua-20190102",
    "desc": "xiaohua",
    "culture": "zh-cn",
    "tokenizerVersion": "1.0.0",
    "intents":intents,
    "entities": [],
    "composites": [],
    "closedLists":closedLists,
    "patternAnyEntities": [],
    "regex_entities": [],
    "prebuiltEntities": [],
    "model_features": [],
    "regex_features": [],
    "patterns": [],
    "utterances":utterances,
    "settings": []
    }
    json_str_luis = json.dumps(luisdata,indent=2, ensure_ascii=False)
    with open("{0}/merge-luis.json".format(TARGET_PATH), "w",encoding='utf-8') as f:
        f.write(json_str_luis)


if __name__ == '__main__':
    filepaths = lookupdir()
    for filepath in filepaths:
        readfile(filepath)
    np.random.shuffle(utterances)
    np.random.shuffle(intents)
    writeluisinfile()
    writeinrasafile()
    print("rasa文件以及luis文件合并且随机排序完毕！")