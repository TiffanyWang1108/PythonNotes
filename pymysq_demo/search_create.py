import sys

from pymysq_demo.get_con_Demo import get_conn


def test_search():
    conn = get_conn()
    cursor = conn.cursor()

    sql = "select * from tb_create;"

    try:
        cursor.execute(sql)
        # records = cursor.fetchone() # 获取单条记录
        # records = cursor.fetchmany(2) # 获取多条记录
        records = cursor.fetchall()  # 获取所有数据
        print(records)
    except Exception as e:
        print(sys.exc_info())
    finally:
        conn.close()
        print("Close")
