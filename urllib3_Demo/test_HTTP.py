import urllib3


def test_HTTP():
    # 创建连接池对象， 默认会校验证书
    pm = urllib3.PoolManager()
    # 发送HTTP请求
    response = pm.request(method="GET", url="http://httpbin.org/get")
    print(type(response))

    print(response.status)  # 查看响应状态码
    print(response.headers)  # 查看响应头信息
    print(response.data)  # 查看响应园时二进制信息
