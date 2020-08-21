def func():
    for i in range(0,3):
        print("开始迭代")
        yield i
        print("一次迭代结束")
 
# f = func()
# print(f.__next__())
# f.send(1011)
# print(f.__next__())

# for i in range(0,3):
#     print(i)
left_lemmas = ['a','b','c']
print(left_lemmas[-1:])

for i in range(0,3):
        print("开始迭代")
        print(i)
        print("一次迭代结束")