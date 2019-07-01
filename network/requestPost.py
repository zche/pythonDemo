import requests
import json

mydata={'wd':'linux','name':'xwp'}
r = requests.post("http://httpbin.org/post",data=mydata)
r = requests.post("http://httpbin.org/post",data=json.dumps(mydata))
