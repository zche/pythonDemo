dic = {'x':1,'y':2,'z':3}
for key in dic:
    print(key)
tmp_dic = {
    key: value
    for key,value in dic.items()
}
print(tmp_dic)

if 'x' in dic:
    print('x在字典里')