import yaml

# 定义python对象
data = {
    "client": {"default-character-set": "utf8"},
    "mysql": {"user": 'root', "password": 123},
    "custom": {
        "user1": {"user": "张三", "pwd": 666},
        "user2": {"user": "李四", "pwd": 999},
    }
}
# 直接 dump 可以把对象转为 YAML 文档
with open('./my.yaml', 'w', encoding='utf-8') as f:
    # 如果写入内容包含中文 ==> allow_unicode=True
    yaml.dump(data, f, allow_unicode=True)
