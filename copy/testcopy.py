import copy
a = [1,2,3,4,['a','b']]  #原始对象

b = a  #赋值，传对象的引用

c = copy.copy(a)

d = copy.deepcopy(a)

a.append(5)
a[4].append('c')

print ('a=',a)
#a= [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print ('b=',b)
#b= [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# c 是浅copy，不会copy子对象，故['a','b'] 这个数组子对象只当引用拷贝了过去，所以a[4].append('c')会体现到c的值上
print ('c=',c)
#c= [1, 2, 3, 4, ['a', 'b', 'c']]
#而d是深copy，['a','b'] 这个数组子对象也当值copy了过去，所以，当原始的这个数组对象发生改变的时候，并不会影响d的值内容
print ('d=',d)
#d= [1, 2, 3, 4, ['a', 'b']]