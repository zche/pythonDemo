import glob
import os
print(glob.glob(r'*'))
path = '/Users/zhaoruifei/Work/Pactera/NLP/ssoc/Rasa_NLU/projects/default'
model = 'default'
print(os.path.relpath(model,path))
print(os.path.relpath(model))