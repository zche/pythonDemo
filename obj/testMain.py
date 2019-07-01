import test
worker = test.Test('zhangsan',10000)
print(type(worker))
print(worker.hello())
print('end')
print(test.Test.classSpec)
print(hasattr(worker,'classSpec'))