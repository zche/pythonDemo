import numpy as np

__author__ = 'check'

_row =1000
X = 2 * np.random.rand(_row,1)
y = 4 + 3*X + np.random.randn(_row,1)
# np.ones((_row,1))对应X0,X对应X1 
X_b = np.c_[np.ones((_row,1)),X]

learing_rate = 0.1
n_iterations = 1000
m = _row

# 初始化theta值---随机一个2行一列的矩阵（标准正态分布的矩阵）
theta = np.random.randn(2,1)
count =0 

for iteration in range(n_iterations):
    count +=1
    #  求梯度 X^T*(X*theta-y)
    gradients = 1/m * X_b.T.dot(X_b.dot(theta)-y)
    theta = theta - learing_rate * gradients

print(count)
print(theta)