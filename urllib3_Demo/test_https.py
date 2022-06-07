import urllib3
import json


def test_HTTPS():
    # 创建不校验证书的连接池对象
    pm_https = urllib3.PoolManager(cert_reqs="CERT_NONE")
    url = "https://httpbin.ceshiren.com/get"

    # 发送HTTPS请求
    resp = pm_https.request(method='GET', url=url)
    print(json.dumps(resp.data.decode('utf-8')))
