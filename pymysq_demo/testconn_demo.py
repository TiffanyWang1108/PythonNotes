import pymysql

from .get_con_Demo import get_conn


def test_demo():
    # 1.打开连接
    conn = get_conn()
    print("打开成功")
    # 2.获取游标
    cursor = conn.cursor()
    # 3. 执行SQL
    cursor.execute("select version();")
    # 4.获取结果
    version = cursor.fetchone()
    print(version)
    conn.close()
