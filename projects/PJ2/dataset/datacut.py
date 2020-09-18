import json
import sys
from collections import OrderedDict


with open('heritage_data.json', encoding='UTF8') as json_file:
  json_data = json.load(json_file)

cut_l = ["16", "17", "22", "80"]
heritage_data_make = []
a = []
for i in json_data:
  a.append(i)
for i in a:
    if json_data[i]["ccbaKdcd"] not in cut_l:
        ccbaMnm1 = json_data[i]["ccbaMnm1"]
        ccbaMnm2 = json_data[i]["ccbaMnm2"]
        content = json_data[i]["content"]
        imageUrl = json_data[i]["imageUrl"]
        longitude = json_data[i]["longitude"]
        latitude = json_data[i]["latitude"]
        ccceName = json_data[i]["ccceName"]
        ccbaLcad = json_data[i]["ccbaLcad"]
        ccmaName = json_data[i]["ccmaName"]
        ccbaKdcd = json_data[i]["ccbaKdcd"]
        ccbaCtcd = json_data[i]["ccbaCtcd"]
        ccbaCpno = json_data[i]["ccbaCpno"]

        if ccceName == " ":
            ccceName = "시대 미상"
        heritage_data_make.append(
            {
                "model": "heritage.heritage",
                "pk": ccbaCpno,
                "fields": {
                    "k_name": ccbaMnm1,
                    "h_name": ccbaMnm2,
                    "content": content,
                    "imageurl": imageUrl,
                    "longitude": longitude,
                    "latitude": latitude,
                    "era": ccceName,
                    "address": ccbaLcad,
                    "clsfc_code": ccbaKdcd,
                    "clsfc_name": ccmaName,
                    "sido": ccbaCtcd
                }

            }
        )


with open("heritage_data_made_cut.json", "w", encoding="utf-8") as make_file:
    json.dump(heritage_data_make, make_file, ensure_ascii=False, indent="\t")