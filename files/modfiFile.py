

filePath = "/Users/zhaoruifei/Study/python/files/run.sh"
targetFilePath = "/Users/zhaoruifei/Study/python/files/run.sh.baks"

def writeRunFile(path,content):
    fo = open(path, "w")
    fo.write(content)
    fo.close()

def readFile(path):
    fileContent = ''
    f = open(path, "r")
    line = f.readline()
    while line:
        if "num_train_epochs" in line:
            line = "--num_train_epochs " + 12 + "\"
        if "iterations_per_loop" in line:
            line = "--iterations_per_loop " + 1200 + "\"
        if "num_train_epochs" in line:
            line = "--num_train_epochs " + 12 + "\"
        if "num_train_epochs" in line:
            line = "--num_train_epochs " + 12 + "\"
        fileContent += line
        # print(type(line))
        line = f.readline()
    f.close()
    return fileContent

fileContent = readFile(filePath)
writeRunFile(targetFilePath,fileContent)
