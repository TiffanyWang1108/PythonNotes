import urllib3
import json


# 定制请求数据

def test_headers():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/get"

    # 定制请求头
    headers = {"School": "hogwarts"}
    # 发送请求
    resp = pm.request("GET", url, headers=headers)
    # 查看响应信息
    content = json.loads(resp.data.decode("utf-8"))
    print(type(content), content)
    print(content["headers"])
