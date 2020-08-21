# dic = {'x':1,'y':2,'z':3}
# for key in dic:
#     print(key)
# tmp_dic = {
#     key: value
#     for key,value in dic.items()
# }
# print(tmp_dic)

# if 'x' in dic:
#     print('x在字典里')

# a=[12,3,4,6,7,13,21]
# newList =[x for x in a if x%2==0]
# print(newList)
# value = 'O'
# bilou = [value for _ in '上海，离职了，干什么']
# print(bilou)

a=[12,3,4,6,7,13,21]
print(len(a))
for ind, val in enumerate(a):
    if ind+1<len(a) and a[ind]+1 == a[ind+1]:
        print("第{m}个值和第{n}个值相差1".format(m=ind+1,n=ind+1+1))
