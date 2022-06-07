from pymysq_demo.get_con_Demo import get_conn


# def test_update():
#     conn = get_conn()
#     cursor = conn.cursor()
#
#     sql = "update tb_create set owner='IG' where id=1;"
#
#     try:
#         cursor.execute(sql)
#         conn.commit()
#         print("Update success")
#     except:
#         conn.rollback()
#         print("Rollback")
#     finally:
#         conn.close()
#         print("Close")


def test_delete():
    conn = get_conn()
    cursor = conn.cursor()

    sql = "delete from tb_create where id=1;"

    try:
        cursor.execute(sql)
        conn.commit()
        print("delete success")
    except:
        conn.rollback()
        print("Rollback")
    finally:
        conn.close()
        print("Close")
