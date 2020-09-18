import json
from collections import OrderedDict
import requests
from bs4 import BeautifulSoup
with open('heritage_data1.json', encoding='UTF8') as json_file:
  json_data = json.load(json_file)
# print(type(json_data))
a = []
image_data = OrderedDict()
for i in json_data:
  a.append(i)



for i in a:
    # print(json_data[i])
   
    ccbaKdcd = json_data[i]["clsfc_code"]
    ccbaAsno = json_data[i]["selnum"]
    ccbaCtcd = json_data[i]["sidocode"]
   
    data = requests.get(f"http://www.cha.go.kr/cha/SearchImageOpenapi.do?ccbaKdcd={ccbaKdcd}&ccbaAsno={ccbaAsno}&ccbaCtcd={ccbaCtcd}")
    data_soup = BeautifulSoup(data.content, "xml")


    for picture in data_soup:
        imageUrls = picture.find_all("imageUrl")
        image_list = []
        for imageUrl in imageUrls:
            image_list.append(imageUrl.text)

    image_data[ccbaAsno] = image_list
            
print(image_data)
with open("image_data.json", "w", encoding="utf-8") as make_file:
    json.dump(image_data, make_file, ensure_ascii=False, indent="\t")