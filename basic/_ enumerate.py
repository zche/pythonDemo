arr = [2,34,2,8,4,90,37,21]
result = {item for item in enumerate(arr)}
print(result)

entity_list = ['电视', '电视机', 'u盘', '读卡器', '遥控器', '机顶盒']
for word in entity_list:
    num_tv = '电视'.find(word)
    print(num_tv)
    if  num_tv >= 0:
        print("ok")
    else:
        print("not ok")