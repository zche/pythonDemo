# str ='中国， 怎么办理上海公积金提取'
# val = str[0:2]
# print(val)

# arr1 = [['小米','电视','5'],['音箱'],['小米','全面屏','电视','E65A']]
# print(list(iter(arr1))[0])

# str1 = '{潘婷,氨基酸,洗,护,套装,乳液,修护,洗发水,500,ml,搭配,3,分钟,奇迹,护发素,70,ml," ",新旧,包装,随机,发货,，,价格,￥,59.90,，,适合,头皮,：,干性,，,功效,：,水润,。}'
# str2 = '{B-baj,M-baj,M-baj,M-baj,M-baj,M-baj,M-baj,E-baj,B-rong,E-rong,O,B-baj,M-baj,M-baj,E-baj,B-rong,E-rong,O,O,O,O,O,O,O,B-price,E-price,O,O,O,O,O,O,O,O,O,O}'
# print(len(str1[1:-1].split(',')))
# print(len(str2[1:-1].split(',')))
# for item in arr1:
#     print("{name}的长度为:{length}".format(name=item,length=len(item)))
#     for i in item:
#         print(i)
# dict = []
# str1 = "小米,电视,5"
# x = str1.split(",")
# dict.append(x)
# str2 = "音箱"
# x2 = str2.split(",")
# dict.append(x2)
# for i in dict:
#     print(i)

# def match_entitylist(str1,arr):
#     for arr_item in arr:
#         if arr_item[0]== str1:
#            yield arr_item
# v1 = match_entitylist('小米1',arr1)
# v2 = list(v1)
# print(len(v2))

corpus = [['你好坏','你真好'],['你好坏','你真好'],['你好坏','你真好'],['你好坏','你真好']]
for a,b in corpus:
    print(a,b)