import io
import os
import json
import urllib.request
import urllib.error
import urllib.parse
import xlrd
import xlwt
import sys
import importlib
import numpy as np
import pandas as pd
import json


importlib.reload(sys)
TARGET_PATH = "/Users/zhaoruifei/Work/Pactera/NLP/培训数据/tools/qqa"
intents = []
closedLists = []
utterances = []


def GetReadExcel(path):
    rows = []
    df = pd.read_excel(path, None);
    for s in df:
        titles = [c for c in df[s]]
        for v in df[s].values:
            row = []
            row.append(v[1].replace("\n", ""))
            for colName in titles:
                if colName.startswith('相似问法'):
                    ind = titles.index(colName)
                    if v[ind] and type(v[ind]) != float:
                        row.append(v[ind].replace("\n", ""))
            rows.append(row)
    for item in rows:
        intentItem = {
            "name": item[0]
        }
        intents.append(intentItem)
    ques = [q[1:] for q in rows]
    for item in rows:
        for ques in item[1:]:
            uttItem = {
                "text": ques,
                "intent": item[0],
                "entities": []
            }
            utterances.append(uttItem)
    np.random.shuffle(utterances)
    np.random.shuffle(intents)

def writeluisinfile():
    luisdata={
    "luis_schema_version":"2.2.0",
    "versionId": "0.6",
    "name": "qqa-20191219",
    "desc": "qqa",
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
    with open("{0}/bj_2019122702-luis.json".format(TARGET_PATH), "w",encoding='utf-8') as f:
        f.write(json_str_luis)

def writeinrasafile():
    rasadata={
    "rasa_nlu_data": {
       "regex_features": [],
       "entity_synonyms": [],
       "common_examples":utterances
    }
    }
    json_str_rasa = json.dumps(rasadata,indent=2, ensure_ascii=False)
    with open("{0}/bj_2019122702-rasa.json".format(TARGET_PATH), "w",encoding='utf-8') as f:
        f.write(json_str_rasa)

if __name__ == "__main__":
    common_examples = []

    intentMatching = 0
    intentNotMatching = 0
    intentMatchingGreaterThan = 0
    path = "/Users/zhaoruifei/Work/Pactera/NLP/培训数据/tools/qqa/bj_2019122702_OriginData.xlsx"
    rows = GetReadExcel(path)
    writeluisinfile()
    writeinrasafile()
    print("excel生成luis格式文件和rasa格式文件成功！")
