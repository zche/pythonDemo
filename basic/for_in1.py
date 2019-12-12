a=[12,3,4,6,7,13,21]
num_tokens = len(a)
print(num_tokens)
first_indexex = (i for i in range(num_tokens) if i%2==0)
# if 1 != 2:
#     print("yes")
# else:
#     print("no")
for begin_index in first_indexex:
    # end_index = begin_index
    # while end_index < num_tokens:
    #     break
    #     end_index+=1
    #     #break
    #     print(begin_index)
    print(begin_index)