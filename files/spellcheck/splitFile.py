
from datetime import datetime
 
def Main():
    source_file = '/Users/zhaoruifei/git/NLP/spellCheck/JamSpell/test_data/thuc_news.txt'
    target_dir = '/Users/zhaoruifei/git/NLP/spellCheck/JamSpell/test_data/split_thuc_news_dir/'
 
    # 计数器
    flag = 0
 
    # 文件名
    name = 1
 
    # 存放数据
    dataList = []

    # 字符列表
    # wordList = []
 
    print("开始。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
 
    with open(source_file,'r') as f_source:
        for line in f_source:
        #   line = line.strip()
        #   arrWords = sorted(set(list(line)))
        #   for w in arrWords:
        #       if w not in wordList:
        #           wordList.append(w)
          flag+=1
          dataList.append(line)
          if flag >= 100*10000 and line.strip() == '':
              with open(target_dir+"thuc_news_"+str(name)+".txt",'w+') as f_target:
                  for data in dataList:
                      f_target.write(data)
            #   with open(target_dir+"thuc_news_words"+str(name)+".txt",'w+') as f_target1:
            #         f_target1.write("".join(wordList))
              name+=1
              flag = 0
              dataList = []
            #   wordList = []
                
    # 处理最后一批行数少于210万行的
    if len(dataList)>0:
        with open(target_dir+"thuc_news_"+str(name)+".txt",'w+') as f_target:
            for data in dataList:
                f_target.write(data)
 
    print("完成。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
 
if __name__ == "__main__":
    Main()