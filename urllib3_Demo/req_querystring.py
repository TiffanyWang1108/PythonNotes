import urllib3
import json


# GET/HEAD/DELETE 请求
def test_fields():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/get"
    # 定义查询字符串--定义成字典对象
    fields = {'school': 'hogwarts'}
    # 发送请求
    resp = pm.request(method='GET', url=url, fields=fields)
    # 查看响应信息
    content = json.loads(resp.data.decode("utf-8"))
    print(content)


# POST/PUT 请求
def test_urlencode():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/post"
    # 从内置库urllib的parse模块导入编码方法
    from urllib.parse import urlencode

    # POST和PUT请求需要编码后拼接到URL中
    encoded_str = urlencode({'school': 'hogwarts'})
    # 拼接到URL中，发送请求
    resp = pm.request('POST', url=url + "?" + encoded_str)
    # 查看响应信息
    content = json.loads(resp.data.decode("utf-8"))
    print(content)
