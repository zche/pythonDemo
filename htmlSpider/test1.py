import re
pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+.jpg!t')    # 匹配模式

string = '<img src="https://static.d7w.net/Data/file/links/2019/12/5df1fbefc9a64.jpg" style="width:1320px;margin-top: 2px;" /></a></div>'
url = re.findall(pattern,string)
if len(url) > 0:
    print(url[0])
else:
    print('no data')