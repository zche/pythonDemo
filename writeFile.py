import requests
res=requests.get("http://www.baidu.com")
savefile=open("baidu.html","w")
strContent=str(res.content,encoding="utf-8")
savefile.write(strContent)
savefile.close()