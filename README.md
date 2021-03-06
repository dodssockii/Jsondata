## Json data 다루기





#### 📜 Json data 구조 (jejudata.json)



```json
{
    "result": "200",
    "resultMessage": "SUCCESS",
    "totalCount": 3908,
    "resultCount": 3908,
    "pageSize": 100,
    "pageCount": 40,
    "currentPage": 101,
    "items": [
        {
            "alltag": "체험,공용주차장,화장실,무료 WIFI",
            "contentsid": "CNTS_000000000022310",
            "contentscd": {
                "value": "c2",
                "label": "쇼핑",
                "refId": "contentscd>c2"
            },
            "title": "다나한한복 앤 러블리베베",
            "region1cd": {
                "value": "region1",
                "label": "제주시",
                "refId": "region>region1"
            },
            "region2cd": {
                "value": "11",
                "label": "제주시내",
                "refId": "region1>11"
            },
            "address": "제주특별자치도 제주시 도남동 81-10",
            "roadaddress": "제주특별자치도 제주시 연삼로 355",
            "tag": "체험,쇼핑,관광기념품,상점/상가",
            "introduction": "웨딩한복, 혼주한복, 돌잔치 가족한복 등 제주한복대여 및 맞춤 전문점",
            "latitude": 33.492897,
            "longitude": 126.53028,
            "postcode": "63205",
            "phoneno": "064-722-0022",
            "repPhoto": {
                "descseo": "Danahan Hanbok & Lovely Bebe",
                "photoid": {
                    "photoid": 13998,
                    "imgpath": "https://api.cdn.visitjeju.net/photomng/imgpath/201804/30/504e2747-9129-41cc-94d8-3e40cd38d8b5.jpg",
                    "thumbnailpath": "https://api.cdn.visitjeju.net/photomng/thumbnailpath/201804/30/acea75e3-96fe-4c31-b0b6-d8cc5f40c269.jpg"
                }
            }
        },
        
        ...
        
    ]
}
```



공공데이터인 비짓제주에서 API 키를 받아 REST API request 보낸 후 response로 받은 Json 파일이다.

승인받은 후 사용가능하기 때문에 Json data 일부(2개의 items)이다.

비짓제주 사이트 - https://www.visitjeju.net/kr/visitjejuapi



#### 📂 설명

- data_processing.py : json 라이브러리를 이용하여 필요한 Json data를 가져온다. "address" key에서 "제주특별자치도" 문자열을 제외한 나머지 주소만 가져온다.

- mysql_conn_origin.py : pymysql 라이브러리를 이용하여  mysql 데이터베이스와 연결하고 select 한다.
- mysqlconn.py : 필요한 Json data를 mysql 데이터베이스에 적재시킨다.



