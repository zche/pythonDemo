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
    start = time.time()
    for i in range(5):
        res=p.submit(piao,'safly %s' %i,i).result() #同步调用
        print(res)

    p.shutdown(wait=True)
    print('主', os.getpid())

    stop = time.time()
    print(stop - start)