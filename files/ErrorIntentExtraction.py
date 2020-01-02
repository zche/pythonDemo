import asyncio
import xlrd
import random
import json
import io
import math


class Ex():

    def __init__(self):
        print("11")

    def read_Exl(self, path):
        row_value = []
        book = xlrd.open_workbook(path)
        sheet = book.sheet_by_name('Sheet1')
        rows = sheet.nrows
        #cols = sheet.ncols
        for row in range(rows):
            row_value.append(sheet.row_values(row))
        return row_value

    def data_Reduction(self, _list):
        reduction = {}

        for d in _list:
            if d[4]:
                continue

            if d[1] not in reduction:
                ar = []
                ar.append(d[0])
                reduction.setdefault(d[1], ar)
            else:
                value = reduction.get(d[1])
                value.append(d[0])
                reduction[d[1]] = value

        return reduction

    def random_Selection_Intentions(self, dicts):
        drawOutData = {}

        for item in list(dicts.keys()):
            if item is "" :
                continue
            value = dicts.get(item)
            
            #les = random.randint(1, len(value))  # 随机抽取的个数
            les = math.ceil(len(value)/2)
            #les = len(value)
            drawOut = random.sample(value, les)
            drawOutData.setdefault(item, drawOut)

        return drawOutData


def load_Rasa_traning_data(rasapath, luispath,exlpath):

    with open(rasapath, 'r+', encoding='utf-8') as f:
        rasa = json.loads(f.read())
    with open(luispath, 'r+', encoding='utf-8') as f:
        luis = json.loads(f.read())

    ex = Ex()

    exlData = ex.read_Exl(exlpath)
    reductionDic = ex.data_Reduction(exlData[1:])
    rdmdict = ex.random_Selection_Intentions(dicts=reductionDic)

    print(str(rdmdict))

    for item in rdmdict.keys():
        for value in rdmdict[item]:
            rasa_examples_item = {"intent": item,
                                  "text": value, "entities": []}
            isExists = False
            for p in rasa["rasa_nlu_data"]["common_examples"]:
                if p["text"]== value:
                    isExists = True
                else:
                    continue
            if not isExists:
                rasa["rasa_nlu_data"]["common_examples"].append(rasa_examples_item)
                luis["utterances"].append(rasa_examples_item)
    
    random.shuffle(rasa["rasa_nlu_data"]["common_examples"]) #重新随机排序
    random.shuffle(luis["utterances"])
    rasadata = json.dumps(rasa, indent=2, ensure_ascii=False)
    luisdata = json.dumps(luis, indent=2, ensure_ascii=False)

    with open("{0}".format(rasapath), "w", encoding='utf-8') as f:
        f.write(rasadata)
    with open("{0}".format(luispath), "w", encoding='utf-8') as f:
        f.write(luisdata)
    print(r"rasa和luis 追加成功,并且随机排序！")

if __name__ == "__main__":
    rasa_path=r'/Users/zhaoruifei/Work/Pactera/NLP/培训数据/小华/v1.9/testTotrainRasaJson/JXW-rasa.json'
    luis_path=r'/Users/zhaoruifei/Work/Pactera/NLP/培训数据/小华/v1.9/testTotrainRasaJson/JXW-luis.json'
    excel_path=r'./all/xiaohua/result_jxw.xls'

    load_Rasa_traning_data(rasa_path,luis_path,excel_path)