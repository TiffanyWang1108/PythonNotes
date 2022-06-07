# 1.导入库
import pymysql


# 2.建立连接
def get_conn():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='demo',
        charset="utf8mb4"
    )

    return conn
