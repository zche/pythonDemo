import queue

workQueues = queue.Queue(10)
workQueues.put(1)
workQueues.put(2)
print(workQueues)
print(workQueues.get())
if workQueues.empty():
    print("第一次获取消息，队列已经空了")
print(workQueues.get())
if workQueues.empty():
    print("第二次获取消息，队列已经空了")