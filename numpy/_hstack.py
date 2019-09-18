import numpy as np
#它其实就是水平(按列顺序)把数组给堆叠起来，vstack()函数正好和它相反。
a=[1,2,3]
b=[4,5,6,7]
print(np.hstack((a,b)))

# 输出：[1 2 3 4 5 6 ]

a=[[1],[2],[3]]
b=[[1],[2],[3]]
c=[[1],[2],[3]]
d=[[1],[2],[3]]
print(np.hstack((a,b,c,d)))

# 输出：
# [[1 1 1 1]
#  [2 2 2 2]
#  [3 3 3 3]]