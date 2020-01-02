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
import queue as Queue
import threading
import time


importlib.reload(sys)

TIME_OUT = 10000
ThreadPool = ["thd1", "thd2", "thd3", "thd4","thd5","thd6"]
threads = []
WorkQueues = Queue.Queue(10000)
queueLock = threading.Lock()
exitFlag = 0
threadID = 1

intentMatching = 0
intentNotMatching = 0
intentMatchingGreaterThan = 0

ExportData = []


class RequestThread(threading.Thread):
    def __init__(self, threadID, Name, queues):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = Name
        self.queues = queues
       
    def run(self):
        ProcessData(self.name, self.queues)
        time.sleep(0.1)



def ProcessData(thdName, queues):
    queueLock.acquire()
    if not WorkQueues.empty():
        data = queues.get()
        
        interResult = False
        # info = GetRequest(data[0])
        info = "test"
        if(info[0] == data[1]):
            intentMatching = intentMatching+1
            interResult = True
        else:
            intentNotMatching += 1
            interResult = False
        if(info[0] == data[1] and info[1] >= 0.7):
            intentMatchingGreaterThan += 1
            interResult = True

        ExportData.append(
            [data[0], data[1], info[0], info[1], interResult])

        print('\033[{};{};{}m'.format(32, 40, 4) +
                '->  问题：{0} 原始意图：{1} 匹配意图：{2} 分数：{3}'.format(data[0], data[1], info[0], info[1]) + '\033[0m')
    queueLock.release()


def InsertQueue():
    for thdName in ThreadPool:
        thread = RequestThread(threadID, thdName, WorkQueues)
        thread.start()
        threads.append(thread)
        threadID += 1


def FillInQueue(datas):
    queueLock.acquire()
    for data in datas:
        WorkQueues.put(data)
    queueLock.release()


def GetRequest(QueryString="test"):
    try:
        url = r'http://localhost:5000/parse?q={0}'.format(
        urllib.parse.quote(QueryString))
        requestInfo = urllib.request.urlopen(url=url, data=None, timeout=TIME_OUT)
        data = json.loads(requestInfo.read().decode())
        intent = data["topScoringIntent"]["intent"]
        score = data["topScoringIntent"]["score"]
        entities = data["entities"]
        return intent, score, entities
    except Exception as ex:
        print(ex)
        return "",0,None
   

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
    ExportData = [["问题", "原始意图", "匹配的意图结果", "分数", "原始意图与匹配意图是否相等"]]

    path = r"/Users/zhaoruifei/Work/Pactera/NLP/培训数据/小华/v1.9/华泾镇二期模型_V1.9_20190626/CL/CL_测试集_口语.xlsx"
    expath = r"C:/Users/zhaoruifei/Work/Pactera/NLP/培训数据/tools/all/xiaohua/result_cl.xls"
    rows = GetReadExcel(path)

    FillInQueue(rows[1:])
    # while not WorkQueues.empty():
    #     pass
    InsertQueue()

    for t in threads:
        t.join()

    str_1 = r'测试集数据量：{0} 意图匹配量：{1} 意图不匹配量:{2}'.format(
        len(rows)-1, intentMatching, intentNotMatching)
    str_2 = r"意图匹配率：{0}".format(intentMatching/(len(rows)-1))
    str_3 = r"意图不匹配错误率：{0}".format(intentNotMatching/(len(rows)-1))
    str_4 = r"大于0.7分的匹配概率为:{0}".format(
        intentMatchingGreaterThan/intentMatching)
    ExportData.append(["", "", "", "", ""])
    ExportData.append([str_1, "", "", "", ""])
    ExportData.append([str_2, "", "", "", ""])
    ExportData.append([str_3, "", "", "", ""])
    ExportData.append([str_4, "", "", "", ""])
    print("{0} \n {1} \n {2} \n {3}".format(str_1, str_2, str_3, str_4))
    ExportExcel(expath, ExportData)
