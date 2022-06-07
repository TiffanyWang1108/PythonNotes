# 用于存储和交换数据的语法，是一种轻量级的数据交换格式
# 使用场景：接口数据传输 序列化 配置文件
# json结构
# 键值对--dic 数组形式--list
import json

# 定义一个python结构
python_data = {"a": 1, "b": "霍格沃兹", "c": True, "d": False, "e": None, }

# 将python对象编码为 json 字符串--dumps()
# json_data = json.dumps(python_data)
# print(json_data)
# {"a": 1, "b": ["2", "3"], "c": true, "d": false, "e": null}

# 将 JSON 字符串解码为python 对象--loads()
# 定义一个 json 字符串
# json_data = '''{"a": 1, "b": ["2", "3"], "c": true, "d": false, "e": null}'''
# print(type(json_data))  # str
# python_data = json.loads(json_data)
# print(python_data)
# print(type(python_data))  # dict
# {'a': 1, 'b': ['2', '3'], 'c': True, 'd': False, 'e': None}


# PYTHON对象编码，并将数据写入json文件中---dump()
# with open("data.json", "w") as f:
#     json.dump(python_data, f)

# 从json文件中读取数据并解码为python对象
# with open("data.json", "r") as f:
#     data = json.load(f)
#     print(data)

# 转化成为json格式
json_data = json.dumps(python_data)
print(json_data)
# {"a": 1, "b": "\u970d\u683c\u6c83\u5179",}
json_data = json.dumps(python_data, ensure_ascii=False, indent=4)
print(json_data)
