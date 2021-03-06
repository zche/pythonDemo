
from datetime import datetime
 
def Main():
    source_file = '/Users/zhaoruifei/git/NLP/spellCheck/JamSpell/test_data/thuc_news.txt'
    target_file = '/Users/zhaoruifei/git/NLP/spellCheck/JamSpell/test_data/10_127_382700_382712_none_emptyline_thuc_news.txt'
    # 存放数据
    dataList = []
 
    print("开始。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    flagCount = 0
    
    # count = 0
    # index = 0
    # with open(target_file,'r') as f_source:
    #     for line in f_source:
    #         index = index + 1
    #         if len(line) > 500:
    #             count = count + 1


    with open(source_file,'r') as f_source:
        for line in f_source:
            flagCount += 1
            if flagCount < 382700: 
                continue
            if flagCount > 382712:
                break
            tmpLine = line.replace(" ","").replace("\t","").strip()
            if tmpLine == '':
                continue
            targetLine = line.replace("\u3000","").replace("\xa0","").replace(" ","").replace("\t","")
            if len(targetLine) < 10:
                continue
            
            if len(targetLine) > 127:
                dataList.append(targetLine[0:126]+"\n")
            else:
                dataList.append(targetLine)

            
    with open(target_file,'a+') as f_target:
        for data in dataList:
            f_target.write(data)


    # print('索引为：'+ str(index))
    # print('大于500的数量为：'+ str(count))
    print("完成。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
 
if __name__ == "__main__":
    Main()