import datetime

dtStr1 = '2020-05-20 10:00:00'
dt1 = datetime.datetime.strptime(dtStr1[0:10], '%Y-%m-%d')

dtStr2 = '2020-05-20 17:00:00'
dt2 = datetime.datetime.strptime(dtStr2, '%Y-%m-%d %H:%M:%S')

dt3 = datetime.datetime.combine(dt1.date(),dt2.time())

print(str(dt3))