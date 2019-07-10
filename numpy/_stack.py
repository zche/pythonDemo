import numpy as np
# arrays里面的每个元素必须形状是一样的，例如本例中列表a中的两个元素[1,2,3]和[4,5,6]的形状是一样的，
# 如果把[4,5,6]换成[4,5] ，那么程序会报错！而axis代表的是在哪个维度上加一维，
# 例如axis=0(它是默认的)代表的就是增加的这一维的下标为0

# a=[[1,2,3],
#    [4,5,6]]
# print("列表a如下：")
# print(a)

# print("增加一维，新维度的下标为0")
# c=np.stack(a,axis=0)
# print(c)

# print("增加一维，新维度的下标为1")
# c=np.stack(a,axis=1)
# print(c)

# a=[[1,2,3,4],
#    [5,6,7,8],
#    [9,10,11,12]]
# print("列表a如下：")
# print(a)

# print("增加一维，新维度的下标为0")
# c=np.stack(a,axis=0)
# print(c)

# print("增加一维，新维度的下标为1")
# c=np.stack(a,axis=1)
# print(c)

a=[[1,2,3],
   [4,5,6]]
b=[[1,2,3],
   [4,5,6]]
c=[[1,2,3],
   [4,5,6]]
print("a=",a)
print("b=",b)
print("c=",c)

print("增加一维，新维度的下标为0")
d=np.stack((a,b,c),axis=0)
print(d)

print("增加一维，新维度的下标为1")
d=np.stack((a,b,c),axis=1)
print(d)
print("增加一维，新维度的下标为2")
d=np.stack((a,b,c),axis=2)
print(d)