import ast

str1 = '[1.2,3.02,5.1,6.7]'
lst = ast.literal_eval(str1)
for n in lst:
    print(n)