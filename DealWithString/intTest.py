def GetNormalStr(str1):
    if isinstance(str1, bool):
        str1="{val}".format(val=str(str1))
    if isinstance(str1, float):
        str1="{val}".format(val=str(str1))
    if isinstance(str1, int):
        str1="{val}".format(val=str(str1))
    return str1.lstrip().rstrip().replace("\n", "")



print(GetNormalStr(1))