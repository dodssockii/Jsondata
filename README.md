## Json data ๋ค๋ฃจ๊ธฐ





#### ๐ Json data ๊ตฌ์กฐ (jejudata.json)



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
            "alltag": "์ฒดํ,๊ณต์ฉ์ฃผ์ฐจ์ฅ,ํ์ฅ์ค,๋ฌด๋ฃ WIFI",
            "contentsid": "CNTS_000000000022310",
            "contentscd": {
                "value": "c2",
                "label": "์ผํ",
                "refId": "contentscd>c2"
            },
            "title": "๋ค๋ํํ๋ณต ์ค ๋ฌ๋ธ๋ฆฌ๋ฒ ๋ฒ ",
            "region1cd": {
                "value": "region1",
                "label": "์ ์ฃผ์",
                "refId": "region>region1"
            },
            "region2cd": {
                "value": "11",
                "label": "์ ์ฃผ์๋ด",
                "refId": "region1>11"
            },
            "address": "์ ์ฃผํน๋ณ์์น๋ ์ ์ฃผ์ ๋๋จ๋ 81-10",
            "roadaddress": "์ ์ฃผํน๋ณ์์น๋ ์ ์ฃผ์ ์ฐ์ผ๋ก 355",
            "tag": "์ฒดํ,์ผํ,๊ด๊ด๊ธฐ๋ํ,์์ /์๊ฐ",
            "introduction": "์จ๋ฉํ๋ณต, ํผ์ฃผํ๋ณต, ๋์์น ๊ฐ์กฑํ๋ณต ๋ฑ ์ ์ฃผํ๋ณต๋์ฌ ๋ฐ ๋ง์ถค ์ ๋ฌธ์ ",
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



๊ณต๊ณต๋ฐ์ดํฐ์ธ ๋น์ง์ ์ฃผ์์ API ํค๋ฅผ ๋ฐ์ REST API request ๋ณด๋ธ ํ response๋ก ๋ฐ์ Json ํ์ผ์ด๋ค.

์น์ธ๋ฐ์ ํ ์ฌ์ฉ๊ฐ๋ฅํ๊ธฐ ๋๋ฌธ์ Json data ์ผ๋ถ(2๊ฐ์ items)์ด๋ค.

๋น์ง์ ์ฃผ ์ฌ์ดํธ - https://www.visitjeju.net/kr/visitjejuapi



#### ๐ ์ค๋ช

- data_processing.py : json ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ฅผ ์ด์ฉํ์ฌ ํ์ํ Json data๋ฅผ ๊ฐ์ ธ์จ๋ค. "address" key์์ "์ ์ฃผํน๋ณ์์น๋" ๋ฌธ์์ด์ ์ ์ธํ ๋๋จธ์ง ์ฃผ์๋ง ๊ฐ์ ธ์จ๋ค.

- mysql_conn_origin.py : pymysql ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ฅผ ์ด์ฉํ์ฌ  mysql ๋ฐ์ดํฐ๋ฒ ์ด์ค์ ์ฐ๊ฒฐํ๊ณ  select ํ๋ค.
- mysqlconn.py : ํ์ํ Json data๋ฅผ mysql ๋ฐ์ดํฐ๋ฒ ์ด์ค์ ์ ์ฌ์ํจ๋ค.



