import numpy as np
from sklearn.linear_model import Ridge,SGDRegressor

__author__ = 'check'

_row =1000
X = 2 * np.random.rand(_row,1)
y = 4 + 3*X + np.random.randn(_row,1)

ridge_reg = Ridge(alpha=1,solver='auto')
ridge_reg.fit(X,y)
print(ridge_reg.predict(1.5))
print(ridge_reg.intercept_)
print(ridge_reg.coef_)

sgd_reg = SGDRegressor(penalty='l2')#penalty=L2，就是Ridge Regression
sgd_reg.fit(X,y.ravel())
print(sgd_reg.predict(1.5))