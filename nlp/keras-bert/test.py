from keras_bert import extract_embeddings

model_path = '/Users/zhaoruifei/Work/Pactera/NLP/qqa/bert_as_service/bert_as_service/chinese_L-12_H-768_A-12'
texts = ['黄金手啥课对方水电费']
embeddings = extract_embeddings(model_path, texts)
print(embeddings)