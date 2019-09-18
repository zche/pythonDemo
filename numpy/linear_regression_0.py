import numpy as np
import matplotlib.pyplot as plt
#求线性模型的解析解
__author__ = 'check'
_row = 1000
# 这里相当于是随机X维度X1,rand是随机均匀分布 100行1列（0到1之间的数，包括0，记为[0,1),一列代表一个维度，即100个X1数据）
X = 2 * np.random.rand(_row,1)
# 人为的设置真实的Y一列，np.random.randn(100,1)是设置error,randn是标准正太分布（miu为0，方差为1）
# 4+3*X 是Y_hat
# np.random.randn(_row,1) 就是偏差epsilong 
y = 4+3*X + np.random.randn(_row,1)
# 整合X0和X1
# c_就是combine（整合），拼接X0 和 X1,X0是100个1，X1就是随机的100个数字
# X_b 就是X矩阵
X_b = np.c_[np.ones((_row,1)),X]
print(X_b)
# 常规等式求解theta linalg 是线性代数的类库，inv就是inverse(相反的，求逆)
# .T把X_b矩阵转置
# dot就是点积，点乘
# 解析解theta：[(X^T*X)^(-1)]*X^T*y，一步求theta
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
print(theta_best)

# 算出模型后，预测未来
# 创建测试集里面的X1
X_new = np.array([[0],[2]])
X_new_b = np.c_[(np.ones((2,1))),X_new]
print(X_new_b)
# y=X*theta
# X是m行数组，n列特征(维度)的矩阵（m*n），而theta就是n个W值，即（n*1的矩阵），
# X*theta 就是(m*n)的矩阵 * (n*1)的矩阵,所以结果就是 (m*1)的测试结果：矩阵y
# y = X0i*W0 + X1i*W1 + X2i*W2 +...+Xnm*Wm
y_predict = X_new_b.dot(theta_best)
print(y_predict)

# 每个真实值和预测值相减，平方加和，最小的时刻
plt.plot(X_new,y_predict,'r-')
plt.plot(X,y,'b.')
plt.axis([0,2,0,15])
plt.show()