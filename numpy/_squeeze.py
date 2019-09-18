import numpy as np

# numpy.squeeze()函数

# 语法：numpy.squeeze(a,axis = None)

#  1）a表示输入的数组；
#  2）axis用于指定需要删除的维度，但是指定的维度必须为单维度，否则将会报错；
#  3）axis的取值可为None 或 int 或 tuple of ints, 可选。若axis为空，则删除所有单维度的条目；
#  4）返回值：数组
#  5) 不会修改原数组；
# 作用：从数组的形状中删除单维度条目，即把shape中为1的维度去掉

# 引用：https://docs.scipy.org/doc/numpy/reference/generated/numpy.squeeze.html

# 场景：在机器学习和深度学习中，通常算法的结果是可以表示向量的数组（即包含两对或以上的方括号形式[[]]），如果直接利用这个数组进行画图可能显示界面为空（见后面的示例）。我们可以利用squeeze（）函数将表示向量的数组转换为秩为1的数组，这样利用matplotlib库函数画图时，就可以正常的显示结果了。


# demo1
a  = np.arange(10).reshape(1,10)
print(a)
print(a.shape)

# b = np.squeeze(a)
# print(b)
# print(b.shape)

# demo2
# c  = np.arange(10).reshape(2,5)
# print(c)
# print(np.squeeze(c))

# demo3
# d  = np.arange(10).reshape(1,2,5)
# print(d)
# print(d.shape)
# print(np.squeeze(d))
# print(np.squeeze(d).shape)

# 结论：根据上面的3个例子可知，np.squeeze()函数可以删除数组形状中的单维度条目，
# 即把shape中为1的维度去掉，但是对非单维的维度不起作用
