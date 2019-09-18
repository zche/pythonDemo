import numpy  as np
# numpy中的ravel()、flatten()、squeeze()都有将多维数组转换为一维数组的功能，区别： 
# ravel()：如果没有必要，不会产生源数据的副本 
# flatten()：返回源数据的副本 
# squeeze()：只能对维数为1的维度降维
arr = np.arange(12)# arange的步长可以是小数，这是与range的区别
arr1 = arr.reshape(3,4)
# print(arr)
print(arr1)
rav = arr1.ravel()
print(rav)
rav = arr1.flatten()
print(rav)
rav = arr1.squeeze()
print(rav)