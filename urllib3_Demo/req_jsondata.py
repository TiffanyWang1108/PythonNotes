import urllib3
import json


def test_json():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/post"

    # 设定请求数据体类型
    headers = {"Content-Type": "application/json"}
    # 格式化json文本数据
    json_str = json.dumps({"school": "nihao"})
    # 发送请求
    resp = pm.request("POST", url, headers=headers, body=json_str)
    # 解析响应信息
    content = json.loads(resp.data.decode("utf-8"))
    print(content["json"])
