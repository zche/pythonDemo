import re
a = 'Hello,world. ByeBye!'
print(re.sub(r'[A-Z]', '8', a))
# splitres = re.split('123\\b','==123!! abc123. 123. 123abc. 123')
# print(splitres)
# spl1 = re.split('\\b123\\b','123 ==123!! abc123.123.123abc.123')
# print(spl1)

#\b：表示字母数字与非字母数字的边界，     非字母数字与字母数字的边界。(字母数字包括abc等字母以及汉字都属于字母数字，标点符号和空格属于非字母数字)
#\B：表示字母数字与(非非)字母数字的边界，非字母数字与非字母数字的边界。
def _replace_number_blank(text):
        return re.sub(r'\b[0-9]+\b', '0', text).replace(' ', '')
print(_replace_number_blank('abc123def'))
print(_replace_number_blank('abc 123 def'))
print(_replace_number_blank('123'))