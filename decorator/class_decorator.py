from functools import wraps
import sys

print(sys.version_info[0])

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        print("打印日志。。。")
        # logit只打日志，不做别的
        pass

class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''
    def __init__(self, email='admin@myproject.com', logfile='emailout.log',*args, **kwargs):
        self.email = email
        self.logfile = logfile 
        super(logit,self).__init__(*args, **kwargs)

    def notify(self):
        print("发送邮件。。。")
        # 发送一封email到self.email
        # 这里就不做实现了
        pass

# @logit()
# def myfunc1():
#     pass

# myfunc1()

@email_logit()
def myfunc1():
    print('这是myfunc1')
    pass

myfunc1()