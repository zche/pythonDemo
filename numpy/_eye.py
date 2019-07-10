
import numpy as np
 #函数的原型：numpy.eye(N,M=None,k=0,dtype=<class 'float'>,order='C)
# 返回的是一个二维的数组(N,M)，对角线的地方为1，其余的地方为0.
# 参数介绍：
# （1）N:int型，表示的是输出的行数
# （2）M：int型，可选项，输出的列数，如果没有就默认为N
# （3）k：int型，可选项，对角线的下标，默认为0表示的是主对角线，负数表示的是低对角，正数表示的是高对角。
# （4）dtype：数据的类型，可选项，返回的数据的数据类型
# （5）order：{‘C’，‘F'}，可选项，也就是输出的数组的形式是按照C语言的行优先’C'，还是按照Fortran形式的列优先‘F'存储在内存中
a=np.eye(4)
print(a)
print('\n')
a=np.eye(4,k=1)
print(a)
print('\n') 
a=np.eye(4,k=-1)
print(a)
print('\n') 

a=np.eye(4,k=-3)
print(a)
print('\n')
