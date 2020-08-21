#!/Applications/anaconda3/bin/python
# -*- coding: UTF-8 -*-

import requests
import aiohttp
import json
import numpy as np
import uuid

# mydata="{\"id\":\"345\",\"texts\":[\"{str1}\"],\"is_tokenized\":\"false\"}".format(str1=str1)



# mydata="""
# {"id": "1273","texts": ["黄金手"]}
# """


# r = requests.post("http://192.168.1.75:9125/encode",data=mydata)
# print(r)
# print(json.dumps(mydata))
# r = requests.post("http://192.168.1.75:9125/encode",json.dumps(mydata))
# print(r.status_code)


# mydata="{\"id\": \"1273\",\"texts\": [\"hello\"]}"
# mydata="{'id': '1273','texts': ['hello']}"
# mydata='{"id": "1273","texts": ["hello"]}'
# mydata="{\"id\": \"1273\",\"texts\": [\"{str1}\"]}".format(str1=str1)

str1 = "黄金手".encode("utf-8")
url = "http://192.168.1.75:9125/encode"
mydata={'id': '1273','texts': ['黄金手'],'is_tokenized':False}
mydata['id'] = str(uuid.uuid1())
headers = {
  'Content-Type': 'application/json'
}
# response = requests.request("POST", url, headers=headers, data = json.dumps(mydata))
response = requests.post("http://192.168.1.75:9125/encode",headers=headers, data = json.dumps(mydata))
#或者 response = requests.request("POST", url, headers=headers, json = mydata)
result = response.text.encode('utf-8')
dic1 =str(result, encoding = "utf-8")  
data=eval(dic1)
val = data["result"]
npArray = np.array(val)
squeeArray = np.squeeze(npArray)
print(val)