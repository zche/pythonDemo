demolist=[1,2,3,4]
type(demolist)
print(demolist)
print(demolist[1])
demolist[1]=987
print(demolist)
del demolist[1]
print(demolist)
demolist.pop()
print(demolist)
demolist.append(20)
print(demolist)
demolist.append("hello")
print(demolist)
demolist.append(["aa","bb"])
print(demolist)
print(len(demolist))
demolist.pop()
print(demolist)
joinlist = demolist+[100,200]
print(joinlist)
joinlist = demolist * 2
print(joinlist)
if 20 in joinlist:
   print("20在集合中")
