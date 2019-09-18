import random
import time
#python的随机数是假的，因为如果一直调用标准库Random，那么在调用了N次以后，输出结果就会循环最开始的序列了。
# 也就是说，标准库Random所能生成的不同结果的个数也是有限的。32位系统一般也就是几万次以后就会出现重复。

# 为了解决这个问题，这里在每次调用随机函数之前重新设置一下seed为不同的值
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
random.shuffle(arr)
print(arr)
random.seed(time.time())
print(random.random())
print(random.randint(1,10))