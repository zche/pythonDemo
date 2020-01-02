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

importlib.reload(sys)



def GetReadExcel(path):
    row_value = []
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_name('Sheet1')
    rows = sheet.nrows
    #cols = sheet.ncols
    for row in range(rows):
        row_value.append(sheet.row_values(row))
    return row_value


if __name__ == "__main__":
    common_examples = []

    intentMatching = 0
    intentNotMatching = 0
    intentMatchingGreaterThan = 0
    path = "/Users/zhaoruifei/Work/Pactera/NLP/培训数据/小华/v1.9/华泾镇二期模型_V1.9_20190626/common/common_测试集_口语.xlsx"
    exrasapath = "/Users/zhaoruifei/Work/Pactera/NLP/培训数据/小华/v1.9/华泾镇二期模型_V1.9_20190626/common/common_测试集_口语_rasa.json"
    rows = GetReadExcel(path)

    for row in rows[1:]:
        examp_item = {
            "text":row[0],
            "intent":row[1],
            "entities":[]
        }
        common_examples.append(examp_item)
    np.random.shuffle(common_examples)
    rasa_json = {
        "rasa_nlu_data":{
            "regex_features": [],
            "entity_synonyms": [],
            "common_examples": common_examples
        }
    }
    json_str_rasa = json.dumps(rasa_json,indent=2, ensure_ascii=False)
    with open("{0}".format(exrasapath), "w",encoding='utf-8') as f:
        f.write(json_str_rasa)

    print("随机排序，并写入json成功！")
