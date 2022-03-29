import json

def main():
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

        # print(contentsid, title, contentscd_label, address, roadaddress, postcode, phoneno, imgpath, thumbnailpath, latitude, longitude, introduction)

if __name__ == "__main__":
    main()




