import re

msg="我的身份证号是415361199807010070"
regex=r"\d{6}(18|19|20)?\d{2}(0[1-9]|1[012])(0[1-9]|[12]\d|3[01])\d{3}(\d|[xX])"
pattern = re.compile(r"{0}".format(regex), re.I)
m = pattern.search(msg)
if m is not None:
    print(m.group())
    print(m.span())
# if m is not None:
#     matchs.append((m.group(0), m.span(1)))