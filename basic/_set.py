str1 = "你好"
str2 = "你坏"
# if not(set(str1) <= set(str2) or set(str2) <= set(str1)):
#     print('yes')
# else:
#     print('no')

common = set(str1) & set(str2)
print(common)

if set(str1) <= set(str2) or set(str2) <= set(str1):
    print('yes')
else:
    print('no')

# index = 2
# str1 = str(index + 2)
# print(str1)