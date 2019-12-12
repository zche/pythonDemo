import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('^[1-9a-zA-Z]', '11www.runoob.com').span())         # 不在起始位置匹配

regular_v4 = re.findall(r"[t,w]h","https://docs.python.org/3/whatsnew/3.6.html")
print (regular_v4)
# var3 = '''我要学习
# python'''
# print(var3)  # 注意观察输出结果的格式
# print(re.match('/[a-zA-Z]+'))
str1 = '''在/p    １９９８年/t    来临/v  之际/f  ，/w    我/r    十分/m  高兴/a  地/u    通过/p  [中央/n 人民/n  广播/vn 电台/n]/nt      、/w    [中国/ns        国际/n  广播/vn 电台/n]/nt      和/c    [中央/n 电视台/n]]
/nt    ，/w    向/p    全国/n  各族/r  人民/n  ，/w    向/p    [香港/ns        特别/a  行政区/n]/ns    同胞/n  、/w    澳门/ns 和/c    台湾/ns 同胞/n  、/w    海外/s  侨胞/n  ，/w    向/p    世界/n  各国/r  的
/u    朋友/n  们/k    ，/w    致以/v  诚挚/a  的/u    问候/vn 和/c    良好/a  的/u    祝愿/vn ！/w'''
# print(re.sub('x*', '-', 'abxd'))
str2 = re.sub('/[a-zA-Z]+', '', str1)
str3 = re.sub('[\[\]]','',str2)
print(str3)