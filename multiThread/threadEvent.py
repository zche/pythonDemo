import threading
def do(event):
    print('start')
    #函数执行到这里等待信号放行信号
    event.wait()
    #收到放行信号后执行下面的语句
    print('execute')
#实例化threading.Event()事件
event_obj = threading.Event()
for i in range(10):
    t = threading.Thread(target=do, args=(event_obj,))
    t.start()
#先将Flag标识置为False
event_obj.clear()
inp = input('input:')
#如果用户输入'true'就像wait()发送放行信号
if inp == 'true':
    event_obj.set()