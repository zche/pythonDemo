import re
tokens = ['涉及','的','工程','占地','和','淹没区','主要','为','张掖市','肃南','县','境内','的','原','宝瓶','河','牧场','(','现','甘肃','亚盛','实业','(','集团',')','股份','有限','公司','宝瓶','河','分公司',')','和','张掖市','寺大','隆','林场','。']
ner_tags = ['O','O','O','O','O','O','O','O','GPE','GPE','O','O','O','O','O','O','O','O','O','ORG','ORG','ORG','ORG','ORG','O','O','O','O','O','O','O','O','O','GPE','O','O','O','O']
num_tokens = len(ner_tags)
print(num_tokens)
# # find all first indexes of series of tokens tagged as ORG
# 汉字
first_indexes = (i for i in range(num_tokens) if ner_tags[i] == "ORG" and (i == 0 or ner_tags[i-1] != "ORG") and re.match(u'^[\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ffa-zA-Z]+$', str(tokens[i])) != None)
list_indexes = list(first_indexes)
# print(list(first_indexes))
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
