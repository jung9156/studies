Readme

# DB만들기

1. 문화재청 API를 통해 문화재 목록을 뽑고, 그 목록을 토대로 상세 데이터를 조회하여 문화재청에서 제공하는 모든 데이터를 수집

   ```python
   import requests
   from bs4 import BeautifulSoup
   import json
   import sys
   from collections import OrderedDict
   
   # print(data)
   # print(soup.find_all('item'))
   # clsfc_namelist = {"11": "국보", "12": "보물", "13": "사적", "14": "사적및명승", "15": "명승", "16": "천연기념물", "17": "국가무형문화재", "18": "국가민속문화재", "21": "시도유형문화재", "22": "시도무형문화재", "23": "시도기념물", "24": "시도민속문화재", "31": "문화재자료", "79": "등록문화재", "80": "이북5도무형문화재"}
   
   heritage_data = OrderedDict()
   pagenumst = [0, 101, 201, 301, 401, 501, 601, 701]
   pagenumed = [101, 201, 301, 401, 501, 601, 701, 798]
   dirname = ["heritage_data1.json", "heritage_data2.json", "heritage_data3.json", "heritage_data4.json", "heritage_data5.json", "heritage_data6.json", "heritage_data7.json", "heritage_data8.json",]
   for pgn in range(len(pagenumst)):
       for pagenum in range(pagenumst[pgn], pagenumed[pgn]):
   # for pagenum in range(797, 798):
           data = requests.get(f"http://www.cha.go.kr/cha/SearchKindOpenapiList.do?pageUnit=20&pageIndex={pagenum}")
           soup = BeautifulSoup(data.content, "xml")
           for i in soup.find_all("item"):
               no = i.no.text
               ccmaName = i.no.text
               crltsnoNm = i.crltsnoNm.text
               ccbaMnm1 = i.ccbaMnm1.text
               ccbaMnm2 = i.ccbaMnm2.text
               ccbaCtcdNm = i.ccbaCtcdNm.text
               ccsiName = i.ccsiName.text
               ccbaAdmin = i.ccbaAdmin.text
               ccbaKdcd = i.ccbaKdcd.text
               ccbaCtcd = i.ccbaCtcd.text
               ccbaAsno = i.ccbaAsno.text
               ccbaCncl = i.ccbaCncl.text
               ccbaCpno = i.ccbaCpno.text
               longitude = i.longitude.text
   
               datadetail = requests.get(f"http://www.cha.go.kr/cha/SearchKindOpenapiDt.do?ccbaKdcd={ccbaKdcd}&ccbaAsno={ccbaAsno}&ccbaCtcd={ccbaCtcd}")
               soup2 = BeautifulSoup(datadetail.content, "xml")
               
               ccmaName = soup2.ccmaName.text
               gcodeName = soup2.gcodeName.text
               bcodeName = soup2.bcodeName.text
               mcodeName = soup2.mcodeName.text
               scodeName = soup2.scodeName.text
               ccbaQuan = soup2.ccbaQuan.text
               ccbaAsdt = soup2.ccbaAsdt.text
               ccbaLcad = soup2.ccbaLcad.text.strip()
               ccceName = soup2.ccceName.text
               ccbaPoss = soup2.ccbaPoss.text
               ccbaAdmin = soup2.ccbaAdmin.text
               imageUrl = soup2.imageUrl.text
               content = soup2.content.text
   
               heritage_data[ccbaAsno] = {
                   "ccmaName": ccmaName,
                   "crltsnoNm": crltsnoNm,
                   "ccbaMnm1": ccbaMnm1,
                   "ccbaMnm2": ccbaMnm2,
                   "ccbaCtcdNm": ccbaCtcdNm,
                   "ccsiName": ccsiName,
                   "ccbaAdmin": ccbaAdmin,
                   "ccbaKdcd": ccbaKdcd,
                   "ccbaCtcd": ccbaCtcd,
                   "ccbaAsno": ccbaAsno,
                   "ccbaCncl": ccbaCncl,
                   "ccbaCpno": ccbaCpno,
                   "longitude": longitude,
                   "ccmaName": ccmaName,
                   "gcodeName": gcodeName,
                   "bcodeName": bcodeName,
                   "mcodeName": mcodeName,
                   "scodeName": scodeName,
                   "ccbaQuan": ccbaQuan,
                   "ccbaAsdt": ccbaAsdt,
                   "ccbaLcad": ccbaLcad,
                   "ccceName": ccceName,
                   "ccbaPoss": ccbaPoss,
                   "ccbaAdmin": ccbaAdmin,
                   "imageUrl": imageUrl,
                   "content": content,
               }
   
   
       with open(dirname[7], "w", encoding="utf-8") as make_file:
           json.dump(heritage_data, make_file, ensure_ascii=False, indent="\t")
   ```

   

2. 수집한 데이터를 토대로 데이터 가공

   ```markdown
   아직 진행 중
   ```

   

3. 가공한 데이터에서 태그 기준에 맞는 태그 삽입 

   ```markdown
   1 종목이름(국보, 보물 등)
   
   2 문화재 종류(형태(성, 문, 종, 칼, 서적), 무형)
   
   3 시대
   
   4 지역
   
   5 관련인물
   
   
   
   Ex.수원 화성
   
   사적
   
   성
   
   조선
   
   경기도
   
   수원
   
   정조
   
   정약용
   ```

   

4. 태그를 통한 추천 시스템

   ```markdown
   누적된 태그 밸류를 토대로 각 문화재의 점수를 확인, 내림차순으로 추천 예정.
   ```

   



