import io
import os
import json
import numpy as np

WORK_PATH = r'/Users/zhaoruifei/Work/Pactera/NLP/培训数据/小华/v1.9/testTotrainRasaJson/rasa'
TARGET_PATH = r'/Users/zhaoruifei/Work/Pactera/NLP/培训数据/小华/v1.9/testTotrainRasaJson/rasa'

common_examples = []


def lookupdir():
    filepaths = []
    if os.access(path=WORK_PATH, mode=os.R_OK):
        for flieName in os.listdir(WORK_PATH):
            filepaths.append(r'{0}/{1}'.format(WORK_PATH, flieName))
        return filepaths
    else:
        raise Exception("文件不可读或者文件不存在")



def readfile(filepath):
    with open(filepath, 'r+', encoding='utf-8') as f:
        jsonInfo = json.loads(f.read().encode('utf-8').strip())
        for item in jsonInfo["rasa_nlu_data"]["common_examples"]: common_examples.append(item) 
        

def writeinrasafile():
    rasadata={
    "rasa_nlu_data": {
       "regex_features": [],
       "entity_synonyms": [],
       "common_examples":common_examples
    }
    }
    json_str_rasa = json.dumps(rasadata,indent=2, ensure_ascii=False)
    with open("{0}/merge-train-rasa.json".format(TARGET_PATH), "w",encoding='utf-8') as f:
        f.write(json_str_rasa)


if __name__ == '__main__':
    print("合并文件开始时间：{time}".format(time=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))
    filepaths = lookupdir()
    for filepath in filepaths:
        readfile(filepath)
    np.random.shuffle(common_examples)
    writeinrasafile()
    print("rasa测试集文件合并且随机排序完毕！")
    print("合并文件结束时间：{time}".format(time=time.strftime("%Y年%m月%d %H:%M:%S",time.localtime())))