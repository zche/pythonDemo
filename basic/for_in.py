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

a=[12,3,4,6,7,13,21]
newList =[x for x in a if x%2==0]
print(newList)