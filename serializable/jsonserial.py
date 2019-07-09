import json

class testjsonserial(object):
    def __init__(self, *args, **kwargs):
        self.name = 'zrf'
        return super().__init__(*args, **kwargs)

test = testjsonserial().__dict__
obj = {"name": "zxf","obj":{"age":testjsonserial().__dict__}}
result = json.dumps(obj,indent=2,ensure_ascii=False)
print(result)