import tensorflow as tf 

data_id = tf.train.Int64List(value=[int(21)])
data = tf.train.BytesList(value=[bytes(('hello,how are you?'), encoding='utf-8')])
print(data_id)
print(data)
feature_dict = {
            "data_id": tf.train.Feature(int64_list=data_id),
            "data": tf.train.Feature(bytes_list=data)
        }
features = tf.train.Features(feature=feature_dict)
example = tf.train.Example(features=features)
example_str = example.SerializeToString()
print(example_str)