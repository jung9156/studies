import requests
from bs4 import BeautifulSoup
import json
import sys
from collections import OrderedDict

# print(data)
# print(soup.find_all('item'))
# clsfc_namelist = {"11": "국보", "12": "보물", "13": "사적", "14": "사적및명승", "15": "명승", "16": "천연기념물", "17": "국가무형문화재", "18": "국가민속문화재", "21": "시도유형문화재", "22": "시도무형문화재", "23": "시도기념물", "24": "시도민속문화재", "31": "문화재자료", "79": "등록문화재", "80": "이북5도무형문화재"}

pagenumst = [0, 51, 101, 151, 201, 251, 301, 351]
pagenumed = [51, 101, 151, 201, 251, 301, 351, 401]
dirname = ["heritage_data1.json", "heritage_data2.json", "heritage_data3.json", "heritage_data4.json", "heritage_data5.json", "heritage_data6.json", "heritage_data7.json", "heritage_data8.json", "heritage_data9.json", "heritage_dat10.json", "heritage_data11.json", "heritage_data12.json", "heritage_data13.json", "heritage_data14.json", "heritage_data15.json", "heritage_data16.json"]
for pgn in range(len(pagenumst)):
    heritage_data = OrderedDict()
    for pagenum in range(pagenumst[pgn], pagenumed[pgn]):
        print(pagenum)
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
            latitude = i.latitude.text

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

            heritage_data[ccbaCpno] = {
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
                "latitude": latitude,
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

    with open(dirname[pgn], "w", encoding="utf-8") as make_file:
        json.dump(heritage_data, make_file, ensure_ascii=False, indent="\t")