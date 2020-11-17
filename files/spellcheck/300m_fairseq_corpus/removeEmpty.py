
from datetime import datetime
 
 # 存放数据
dataList = []

def Main():
    source_file = '/Users/zhaoruifei/Study/python/files/spellcheck/300m_fairseq_corpus/valid.trg'
    target_file = '/Users/zhaoruifei/Study/python/files/spellcheck/300m_fairseq_corpus/valid.txt'

 
    print("开始。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
 
    # with open(source_file,'r') as f_source:
    #     for line in f_source:
    #         target_line = line.replace(' ','')
    #         dataList.append(target_line)
    #         with open(target_file,'a+') as f_target:
    #             f_target.write(target_line)

    with open(source_file,'r') as f_source:
        for line in f_source:
            target_line = line.replace(' ','')
            dataList.append(target_line)
    with open(target_file,'a+') as f_target:
        for data in dataList:
            f_target.write(data)
                
 
    print("完成。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
 
if __name__ == "__main__":
    Main()