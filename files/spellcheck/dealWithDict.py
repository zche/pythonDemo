import os


WORK_PATH = r'/Users/zhaoruifei/Work/Pactera/拼写检查/other字典语料'
filepaths = []

def getFiles():
    if os.access(path=WORK_PATH, mode=os.R_OK):
        for flieName in os.listdir(WORK_PATH):
            filepaths.append(r'{0}/{1}'.format(WORK_PATH, flieName))
        return filepaths
    else:
        raise Exception("文件不可读或者文件不存在")

def GetWordsByFile(filepath):
    lstWord = []
    with open(filepath, 'r+', encoding='utf-8') as f_read:
        while True:
            line = f_read.readline()
            if not line:
                break
            if 'text' in line and 'count' in line:
                continue
            arr = line.split('"')
            if len(arr) > 3:
                lstWord.append(arr[1])
    return lstWord




if __name__ == '__main__':
    filepaths = getFiles()
    for filepath in filepaths:
        lstWords = GetWordsByFile(filepath)
        print(filepath)
        with open(filepath+"1", 'a+', encoding='utf-8') as f_write:
            for w in lstWords:
                f_write.write(w+'\n')
    print('加工完成！')