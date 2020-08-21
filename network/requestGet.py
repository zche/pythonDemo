import requests

myparams={'imageName':'test1_lala_1','imageVersion':'4.6'}
r=requests.get("http://172.16.37.133/api/nlu/rasa/model/getbyimagenameandversion",myparams)
print(r.ServerIP)
