from pymysq_demo.get_con_Demo import get_conn


# def test_create():
#     conn = get_conn()
#     cursor = conn.cursor()
#     sql = """
#         CREATE TABLE `tb_create` (
#         `id` int(11) NOT NULL AUTO_INCREMENT,
#         `title` varchar(255) COLLATE utf8_bin NOT NULL,
#         `expect` varchar(255) COLLATE utf8_bin NOT NULL,
#         `owner` varchar(255) COLLATE utf8_bin NOT NULL,
#         PRIMARY KEY (`id`)
#     ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
#         """
#     cursor.execute(sql)
#     conn.close()


def test_insert():
    conn = get_conn()
    cursor = conn.cursor()
    sql = "insert into tb_create (id, title, expect, owner) " \
          "values (2, 's11全球总决赛', '冠军', 'EDG');"

    try:
        cursor.execute(sql)
        conn.commit()
        print("success")
    except:
        conn.rollback()
        print("Rollback")
    finally:
        conn.close()
        print("close")
