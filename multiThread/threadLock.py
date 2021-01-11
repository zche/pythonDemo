import threading
gnum=0
lock=threading.RLock()
def work(max_number):
    for i in range(max_number):
        print(i)
def mylock():
    work(10)
    #在操作gnum之前先上锁
    #acquire()的括号里可以定义锁定的timeout时间，超过这个时间就自动打开锁
    lock.acquire()
    global gnum
    gnum=gnum+1
    #操作结束之后再打开锁
    lock.release()
    print('gnum is ',gnum)
for x in range(5):
    t=threading.Thread(target=mylock)
    t.start()