import requests
from bs4 import BeautifulSoup
import json
import sys
from collections import OrderedDict


siteCode_list = {"01": "문화재야행", "1": "문화재야행", "02": "생생문화재", "03": "전통산사문화재", "04": "살아숨쉬는 향교·서원", "07": "국립무형유산원", "08": "한국문화재재단", "09": "고택·종갓집", "10": "세계유산", "06": "기타행사"}
event_data = OrderedDict()
for month in range(1, 13):
    data = requests.get(f"http://www.cha.go.kr/cha/openapi/selectEventListOpenapi.do?searchYear=2020&searchMonth={month}")
    soup = BeautifulSoup(data.content, "xml")
    for i in soup.find_all("item"):
        seqNo = i.seqNo.text
        siteCode = i.siteCode.text
        siteName = siteCode_list[siteCode]
        subTitle = i.subTitle.text
        subContent = i.subContent.text
        sDate = i.sDate.text
        eDate = i.eDate.text
        groupName = i.groupName.text
        contact = i.contact.text
        subDesc = i.subDesc.text
        subPath = i.subPath.text
        subDesc_2 = i.subDesc_2.text
        subDesc_3 = i.subDesc_3.text
        mainImageTemp = i.mainImageTemp.text
        sido = i.sido.text
        gugun = i.gugun.text
        subDate = i.subDate.text

        event_data[seqNo] = {"seqNo": seqNo, "siteCode": siteCode, "siteName": siteName, "subTitle": subTitle, "subContent": subContent, "sDate": sDate, "eDate": eDate, "groupName": groupName, "contact": contact, "subDesc": subDesc, "subPath": subPath, "subDesc_2": subDesc_2, "subDesc_3": subDesc_3, "mainImageTemp": mainImageTemp, "sido": sido, "gugun": gugun, "subDate": subDate}


# print(json.dumps(heritage_data, sort_keys=True, indent=4))
with open("event_data.json", "w", encoding="utf-8") as make_file:
    json.dump(event_data, make_file, ensure_ascii=False, indent="\t")