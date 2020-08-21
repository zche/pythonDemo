str1 = '手机验证码'
list_entities = []
list_entities.append({'end': 6, 'entity': '登录方式', 'start': 1, 'value': '手机验证码'})
list_entities.append({'end': 6, 'entity': '登录方式', 'start': 3, 'value': '验证码'})
for item in list_entities:
    if item['value']!=str1:
        list_entities.remove(item)
print(len(list_entities))