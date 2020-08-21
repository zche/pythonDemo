from globalVal import globalVal

def do_something():
    globalVal.global_list.append('a')
    globalVal.global_list.append('b')
    print('test2.py')
    print(globalVal.global_list)