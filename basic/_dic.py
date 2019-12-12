dict = {}
dict['a'] = 'zrf'
dict['b'] = 'zxf'
for entity in dict:
    print(entity)
    print(dict[entity])

# if ("Hello").lower().find('h') >= 0:
#     print('yes')
# else:
#     print('not')

str1 = "你好"
str2 = "你"
if not(set(str1) <= set(str2) or set(str2) <= set(str1)):
    print('yes')
else:
    print('no')


str1 =''
if not str1.isspace():
    print("bu是空的")
# str1 ="dd"
# flag = False
# if (str1 == None or str1 == '') or flag == False:
#     print('ok')