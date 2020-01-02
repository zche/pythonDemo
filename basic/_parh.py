import os

str = "/Users/zhaoruifei/git/NLP/rasa_nlu_gq-0.2.7/projects/default"
str ="default"
path = os.path.abspath(str)
project = "zrf"
path = os.path.join(os.path.abspath(str), project)
print(path)