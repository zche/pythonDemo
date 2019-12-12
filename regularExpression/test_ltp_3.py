#!/usr/bin/env python
#encoding:utf-8
import re
tokens = ['2','(','二',')','公司','名称',':','甘肃','天润','薯业','有限','责任','公司','法定','代表人',':','张希林','注册','资本',':','3','，','000万','元','注册','地址',':','甘肃省','张掖市','山丹县','山','马路','7','号','经营','范围',':','马铃薯','脱毒','基础','种薯','生产','、','经营','(','凭','有效','许可证','生产','、','经营',')',';']
ner_tags = ['O','O','O','O','O','O','O','B-Ni','I-Ni','I-Ni','I-Ni','I-Ni','E-Ni','O','O','O','S-Nh','O','O','O','O','O','O','O','O','O','O','B-Ns','I-Ns','E-Ns','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O']
num_tokens = len(ner_tags)
num_ners = len(ner_tags)
print(num_tokens)
print(num_ners)
# # find all first indexes of series of tokens tagged as ORG
first_indexes = (i for i in range(num_tokens) if "-Ni" in ner_tags[i] and (i == 0 or "-Ni" not in  ner_tags[i-1]) and re.match(u'^[\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ffa-zA-Z]+$', str(tokens[i])) != None)
list_indexes = list(first_indexes)
print(len(list_indexes))
for begin_index in list_indexes:
    # print(begin_index)
    end_index = begin_index + 1
    # while end_index < num_tokens and ner_tags[end_index] == "ORG" and re.match(u'^[\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ffa-zA-Z]+$', str(tokens[end_index])) != None:
    #     end_index += 1
    # end_index -= 1
    print(end_index)

# first_indexes = (i for i in range(num_tokens))
# print(list(first_indexes))

# if re.match(u'^[\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ffa-zA-Z0-9（）]+$', str("）")) != None:
#     print("yes")
# else:
#     print("no")

# a =1
# if a==1 and (1==0 or 1==1):
#    print("是的")
# else:
#     print("不是的")
