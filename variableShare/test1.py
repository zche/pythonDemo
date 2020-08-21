from test2 import *
from globalVal import globalVal

global_list = globalVal.global_list
if __name__ == '__main__':
    # 这里调用py2.py的方法，往列表中添加元素
    do_something()
    print('test1.py')
    print(global_list)