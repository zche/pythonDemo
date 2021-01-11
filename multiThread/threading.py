import time
import threading

threads=[]
numArr = [3]
def haha(max_num):
    """
    随便定义一个函数，要求用户输入一个要打印数字的最大范围
    输入之后就会从0开始打印，直到用户输入的范围值
    """
    for i in range(max_num):
        """
        每次打印一个数字前要间隔1秒，那么打印10个数就要耗时10秒
        """
        time.sleep(1)
        print(i)
for x in range(3):
    # t=threading.Thread(target=haha,args=(3,)))
    t=threading.Thread(target=haha,args=numArr)
    threads.append(t)
for thr in threads:
    thr.setDaemon(False)
    #把列表中的实例遍历出来后，调用start()方法以线程启动运行
    thr.start()
# for thr in threads:
#     """
#     isAlive()方法可以返回True或False，用来判断是否还有没有运行结束
#     的线程。如果有的话就让主线程等待线程结束之后最后再结束。
#     """
#     if thr.isAlive():
#         thr.join()