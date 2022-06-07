# 读取yaml文件中的内容转化为python对象
import yaml

with open("./my.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

print(data)
print(type(data))

# # 取到user1的姓名--字典取value--取对应的key
# user1_name = data["custom"]["user1"]["user"]
# print(user1_name)
