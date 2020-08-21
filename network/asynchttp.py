import aiohttp
import asyncio
# import json

str1 = "黄金手".encode("utf-8")
url = "http://192.168.1.75:9125/encode"
mydata={'id': '1273','texts': ['黄金手']}
headers = {
  'Content-Type': 'application/json'
}
# response = requests.request("POST", url, headers=headers, data = json.dumps(mydata))
# response = requests.post("http://192.168.1.75:9125/encode",headers=headers, data = json.dumps(mydata))

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post(url,headers=headers,json = mydata) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            result = await response.text()
            # dic1 =str(result, encoding = "utf-8")  
            data=eval(result)
            print(data["result"][0])

            html = await response.text()
            print("Body:", html[:15], "...")

loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_until_complete(task)