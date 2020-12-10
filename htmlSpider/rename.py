import os

path = "/Users/zhaoruifei/Downloads/tmp/pictures"
fileList=os.listdir(path)
for oldname in fileList:
    if '.jpg' in oldname:
        oldname = os.path.join(path, oldname)
        newname = oldname.replace('!t','')
        os.rename(oldname, newname)
        print(oldname)
        print(newname)