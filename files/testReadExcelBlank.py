import argparse
import logging
from functools import wraps

import simplejson
import six
import numpy as np
from builtins import str
from pydantic import BaseModel
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED
from starlette.responses import JSONResponse,FileResponse
import pandas as pd
import copy
import json
import time
import tempfile
import os
import paramiko
import urllib.request
import urllib.error
import urllib.parse
import xlrd
import xlwt
import subprocess
import requests
import yaml

logger = logging.getLogger(__name__)

intents = []
closedLists = []
utterances = []
synonymsList = []
imgRepoAddress = "192.168.1.102/hightalk-nlu-test"
getModelInfoAddress = "http://192.168.1.75:17777/api/nlu/rasa/model/getbyimagenameandversion"

def GetNormalStr(str1):
    if isinstance(str1, bool):
        str1="{val}".format(val=str(str1))
    if isinstance(str1, float):
        str1="{val}".format(val=str(str1))
    if isinstance(str1, int):
        str1="{val}".format(val=str(str1))
    return str1.lstrip().rstrip().replace("\n", "")

def GetReadExcelForIntents(path):
    dicts = {}
    sheetName = '训练集'

    df = pd.read_excel(path,None);
    if sheetName not in df.keys():
        sheetName='临时训练集' 
    for v in df[sheetName].values:
        ques = GetNormalStr(v[0]).lower()
        intent = GetNormalStr(v[1])
        if(ques =='question' and intent=='intent'):
            continue
        if intent in dicts:
            dicts[intent].append(ques)
        else:
            row = []
            row.append(ques)
            dicts[intent] = row
    for key in dicts:
        intentItem = {
            "name": key
        }
        intents.append(intentItem)
        for item in dicts[key]:
           uttItem = {
                "text": item,
                "intent": key,
                "entities": []
            }
           utterances.append(uttItem) 
    np.random.shuffle(utterances)
    np.random.shuffle(intents)

def GetReadExcelForLists(path):
    dicts = {}
    sheetName = 'entity列表'
    df = pd.read_excel(path, None);
    strName = ''

    for v in df[sheetName].values:
        if pd.isnull(v[0]):
            name = strName
        else:
            name = GetNormalStr(v[0])
        canonicalForm = GetNormalStr(v[1])
        lst = GetNormalStr(v[2])
        if(name =='name' and canonicalForm=='canonicalForm' and lst=='list'):
            continue
        subObj =  {}
        subLst = [x.lower() for x in lst.split(',') if x]
        subObj[canonicalForm] = subLst
        if name in dicts:
            dicts[strName].append(subObj)
        else:
            strName = name
            row = []
            row.append(subObj)
            dicts[name] = row
    return dicts

def writeinclosedlists(dicts):
    for key in dicts:
        subLists =  []        
        for item in dicts[key]:
            (canonicalForm,lists), = item.items()
            subLstJson ={
                "canonicalForm": canonicalForm,
                "list": lists
            } 
            synonymsItem = []
            synonymsItem.append(canonicalForm)
            synonymsItem.extend(lists)
            synonymsList.append(synonymsItem)

            subLists.append(subLstJson)
        closedListItem = {
            "name": key,
            "subLists": subLists
        }
        closedLists.append(closedListItem)
    # print(closedLists)

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
    luisFile = tempfile.gettempdir() + '/' + str(time.time_ns())+".json"
    with open(luisFile, "w",encoding='utf-8') as f:
        f.write(json_str_luis)
    return luisFile

def createluisfile(path):
    GetReadExcelForIntents(path)
    dicts = GetReadExcelForLists(path)
    writeinclosedlists(dicts)
    synDict = {}
    for row in synonymsList:
        for syn in row:
            for item in utterances:
                if syn in item['text']:
                    # tmp = {}

                    # tmp['text'] = item
                    tmp = copy.deepcopy(item)
                    tmp['ent'] = syn
                    synDict[syn] = tmp
                    break
                else:
                    synDict[syn] = None
    omissive = [key for key, value in synDict.items() if value is None]
    
    if len(synonymsList)>0:
        for row in synonymsList:
            otherArr = []
            for item in omissive:
                if item in row:
                    otherArr.append(item)
            ret = list(set(row).difference(set(otherArr)))
            if len(otherArr) == 0:
                continue
            if len(ret) == 0:
                raise Exception("同义词{ent}相关的列表至少有一个在训练集中".format(ent=row[0]))
            for other in otherArr:
                tmp = copy.deepcopy(synDict[ret[0]])
                tmp['text'] = tmp['text'].replace(tmp['ent'],other)
                tmp.pop('ent')
                utterances.append(tmp)

        handleEntities = []
        entityList = np.concatenate(synonymsList)
        for ent in entityList:
            isEntNotLast = False
            isEntNotFirst = False
            entUtteList = [u for u in utterances if ent in  u['text']]
            if len(entUtteList) == 0:
                raise Exception("同义词{ent}至少要出现在在训练集中一次".format(ent=ent))
            for u in entUtteList:
                if u['text'].index(ent)>0:
                    isEntNotFirst = True
                if (u['text'].rindex(ent)+len(ent)) < len(u['text']):
                    isEntNotLast = True
            if not isEntNotFirst or not isEntNotLast:
                tmp = copy.deepcopy(entUtteList[0])
                tmp['text'] = ("啊了"+tmp['text']+"啊了")
                utterances.append(tmp)
                
    luisFile = writeluisinfile()
    return luisFile


luisFile = createluisfile('/Users/zhaoruifei/Downloads/宝洁模板/TrainSet_Test.xlsx')