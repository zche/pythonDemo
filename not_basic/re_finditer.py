
import re
# 从指定的文本中查找符合正则表达式的所有数据的起始位置
text = 'http://blogcsdn.net/caimouse abbaaabbbbaaaaa'
 
pattern = 'ab'
matches = re.finditer(pattern, text)
# print(list(matches))
for match in matches:
    s = match.start()
    e = match.end()
    print('Found {!r} at {:d}:{:d}'.format(text[s:e], s, e))