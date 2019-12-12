def square(x) :            # 计算平方数
         return x +'a'
value = map(square, ['a','b','c','d','e'])   # 计算列表各个元素的平方
text = "".join(list(value))
# # text = [t for t in value]
# text = list(value)
# lala = "".join(text)
print(text)