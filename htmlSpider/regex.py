import os
import re


WORK_PATH = r'/Users/zhaoruifei/Downloads/tmp/pictures/files'
targetFile= r'/Users/zhaoruifei/Downloads/tmp/pictures/urls.txt'
filepaths = []
imgsUrl = []
PATTERN = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+.jpg!t')    # 匹配模式

def getFiles():
    if os.access(path=WORK_PATH, mode=os.R_OK):
        for flieName in os.listdir(WORK_PATH):
            filepaths.append(r'{0}/{1}'.format(WORK_PATH, flieName))
        return filepaths
    else:
        raise Exception("文件不可读或者文件不存在")

def GetUrlByFile(filepath):
    with open(filepath, 'r+', encoding='utf-8') as f_read:
        while True:
            line = f_read.readline()
            if not line:
                break
            url = re.findall(PATTERN,line)
            if len(url) > 0:
                imgsUrl.append(url[0])




if __name__ == '__main__':
    filepaths = getFiles()
    for filepath in filepaths:
        GetUrlByFile(filepath)
    with open(targetFile, 'a+', encoding='utf-8') as f_write:
        f_write.write(str(imgsUrl))
    print(len(imgsUrl))