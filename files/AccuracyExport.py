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

importlib.reload(sys)

TIME_OUT = 10000


def GetRequest(QueryString="test"):
    #url = r'http://192.168.50.28:5000/parse?TenanetID=TZSB&BotRecordId=TZSB&q={0}'.format(urllib.parse.quote(QueryString))
    url = r'http://192.168.1.75:9000/parse?BotRecordId=default&TenanetID=default&q={0}'.format(urllib.parse.quote(QueryString.lower()))
    requestInfo = urllib.request.urlopen(url=url, data=None, timeout=TIME_OUT)
    data = json.loads(requestInfo.read().decode())
    intent = data["topScoringIntent"]["intent"]
    score = data["topScoringIntent"]["score"]
    entities = data["entities"]
    return intent, score, entities


def ExportExcel(path, data):
    index = len(data)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Sheet1')
    for row in range(0, index):
        for col in range(0, len(data[row])):
            sheet.write(row, col, data[row][col])
    workbook.save(path)
    print("数据报表生成完毕")


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
    data = [["问题", "原始意图", "匹配的意图结果", "分数", "原始意图与匹配意图是否相等"]]

    intentMatching = 0
    intentNotMatching = 0
    intentMatchingGreaterThan = 0
    path = "/Users/zhaoruifei/Work/Pactera/NLP/培训数据/tools/qqa/bj_helpdesk_20191227测试集.xlsx"
    #path = "/Users/zhaoruifei/Work/Pactera/NLP/培训数据/小华/v1.9/华泾镇二期模型_V1.9_20190626/CL/CL_测试集_口语.xlsx"
    expath = "/Users/zhaoruifei/Work/Pactera/NLP/培训数据/tools/qqa/Result_bj_2019122704测试集.xls"
    rows = GetReadExcel(path)

    for row in rows[1:]:
        interResult = False
        info = GetRequest(row[0])
        if(info[0].lstrip().rstrip() == row[1].lstrip().rstrip()):
            intentMatching = intentMatching+1
            interResult = True
        else:
            intentNotMatching = intentNotMatching+1
            interResult = False
        if(info[0].lstrip().rstrip() == row[1].lstrip().rstrip() and info[1] >= 0.7):
            intentMatchingGreaterThan = intentMatchingGreaterThan+1
            interResult = True

        data.append([row[0], row[1], info[0], info[1], interResult])
        print('\033[{};{};{}m'.format(32, 40, 4) +
              '问题：{0} 原始意图：{1} 匹配意图：{2} 分数：{3}'.format(row[0], row[1], info[0], info[1]) + '\033[0m')

    str_1 = r'测试集数据量：{0} 意图匹配量：{1} 意图不匹配量:{2}'.format(
        len(rows)-1, intentMatching, intentNotMatching)
    str_2 = r"意图匹配率：{0}".format(intentMatching/(len(rows)-1))
    str_3 = r"意图不匹配错误率：{0}".format(intentNotMatching/(len(rows)-1))
    str_4 = r"大于0.7分的匹配概率为:{0}".format(intentMatchingGreaterThan/intentMatching)
    data.append([str_1, "", "", "", ""])
    data.append([str_2, "", "", "", ""])
    data.append([str_3, "", "", "", ""])
    data.append([str_4, "", "", "", ""])
    print("{0} \n {1} \n {2} \n {3}".format(str_1, str_2, str_3, str_4))
    ExportExcel(expath, data)
