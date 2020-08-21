import glob
import os

strFlag = 'model.ckpt-'
path = os.path.join('/Users/zhaoruifei/Downloads/rasa_model_output', strFlag+'*.meta')
tmp = glob.glob(path)
numArray = []
if len(tmp)>1:
    for f in tmp:
        numArray.append(f[f.index(strFlag)+len(strFlag):-5])
    maxNum = max(numArray)
    for f in tmp:
        num = f[f.index(strFlag)+len(strFlag):-5]
        if num != maxNum:
            tmpFlag=strFlag+str(num)
            delFiles=glob.glob(os.path.join('/Users/zhaoruifei/Downloads/rasa_model_output', tmpFlag+'*'))
            for item in delFiles:
                os.remove(item)

print(tmp)