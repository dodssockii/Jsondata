import pymysql
import json

def insertsql_from_json():
    #접속
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="ssafy123", db="boonmoja", charset="utf8")

    # 커서 가져오기
    cursor = conn.cursor()

    # SQL문 만들기
    sql = "SELECT * FROM user"
    cursor.execute(sql)

    result = cursor.fetchall()
    for res in result:
        print(res)
    conn.commit()
    conn.close()


insertsql_from_json()
