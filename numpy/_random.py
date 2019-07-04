import numpy as np

a = np.arange(5)
print(a)
# shuffle会把原始数组打乱顺序,并且没有返回值
b = np.random.shuffle(a)
print(a)
print(b)
a = np.arange(5)
print(a)
# permutation不会打乱原始数组的顺序，会返回一个新的打乱的数组
b = np.random.permutation(a)
print(a)
print(b)
