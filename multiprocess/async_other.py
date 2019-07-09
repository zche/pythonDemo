from concurrent.futures import ProcessPoolExecutor
import time, random, os
import multiprocessing
multiprocessing.set_start_method('spawn',True)

def piao(name, n):
    print('%s is piaoing %s' % (name, os.getpid()))
    time.sleep(1)
    return n ** 2


if __name__ == '__main__':
    p = ProcessPoolExecutor(2)
    objs = []
    start = time.time()
    for i in range(5):
        obj = p.submit(piao, 'safly %s' % i, i)  # 异步调用
        objs.append(obj)

    for obj in objs:
        print(obj.result())


    p.shutdown(wait=True)
    print('主', os.getpid())


    stop = time.time()
    print(stop - start)