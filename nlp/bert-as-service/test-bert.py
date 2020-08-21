from bert_serving.client import ConcurrentBertClient
import numpy as np
import time


bc = ConcurrentBertClient(ip='127.0.0.1', port=5555,port_out=5556)

num =1
start = time.time()
lst = []

while num<900:
    bert_embedding = bc.encode(['黄金手'], is_tokenized=False)

    # str1 = np.squeeze(bert_embedding)
    lst.append(bert_embedding)
    num=num+1
end = time.time()
strMsg = "总共花费 %.3f s" % (end - start)
print(strMsg)
print(len(lst))