import pymysql
import json

def insertsql_from_json():
    #접속
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="ssafy123", db="boonmoja", charset="utf8")

    # 커서 가져오기
    cursor = conn.cursor()

    with open(".\\jejudata.json", encoding="UTF-8") as json_file:
        jeju_datas = json.load(json_file)

    for jeju_items in jeju_datas["items"]:
        contentsid = jeju_items["contentsid"]
        contentscd_label = jeju_items["contentscd"]["label"]
        title = jeju_items["title"]
        latitude = jeju_items["latitude"]
        longitude = jeju_items["longitude"]

        if jeju_items["address"] is None:
            address = "Null"
        else:
            # address = jeju_items["address"] # 없는 경우 있음
            if "제주특별자치도" == jeju_items["address"][:7]:
                address = jeju_items["address"][8:]
                # print(address)
            else:
                address = jeju_items["address"]
                # print(address)

        if jeju_items["roadaddress"] is None:
            roadaddress = "Null"
        else:
            roadaddress = jeju_items["roadaddress"] # 없는 경우 있음

        if jeju_items["postcode"] is None:
            postcode = "Null"
        else:
            postcode = jeju_items["postcode"] # None 있음

        if jeju_items["phoneno"] is None:
            phoneno = "Null"
        else:
            phoneno = jeju_items["phoneno"].split("/")[0] # None 있음 / 전화번호 여러개 있음 (첫번째 하나)

        if jeju_items["repPhoto"] is not None:
            imgpath = jeju_items["repPhoto"]["photoid"]["imgpath"]
            thumbnailpath = jeju_items["repPhoto"]["photoid"]["thumbnailpath"]
        else:
            imgpath = "Null"
            thumbnailpath = "Null"

        if jeju_items["introduction"] is not None:
            introduction = jeju_items["introduction"]
        else:
            introduction = "Null"

        # SQL문 만들기
        # sql = "SELECT * FROM user"
        sql = "insert into contents(contents_id, address, img_path, introduction, label, latitude, longitude, phone_no, post_code, road_address, thumbnail_path, title) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (contentsid, address, imgpath, introduction, contentscd_label, latitude, longitude, phoneno, postcode, roadaddress, thumbnailpath, title)

        cursor.execute(sql, val)
        conn.commit()

    print(cursor.rowcount, "record inserted")

    # result = cursor.fetchall()
    # for res in result:
    #     print(res)
    # conn.commit()
    # conn.close()


insertsql_from_json()
