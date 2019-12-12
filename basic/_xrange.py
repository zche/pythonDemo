entity_list = ['电视', '电视机', 'u盘', '读卡器', '遥控器', '机顶盒']
mention_text = "".join(map(lambda i: entity_list[i], range(1, 2)))
print(mention_text)