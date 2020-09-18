import requests
from bs4 import BeautifulSoup
api_key = '1hpnPz8Jxw25AJsm1RyotaPLxE0S2M9KJxnMKW4je19Z%2Br%2FLPT6dV%2F%2F3EQQ%2BhLvStDQmi0gp5PLQ8%2FGCC7sPng%3D%3D'
url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey={api_key}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6'

response = requests.get(url).text

data = BeautifulSoup(response, 'html.parser')

items = data.find_all('item')

location = items[7]
# print(items[7])

station = location.stationname.text
# print(location.stationname.text)

dust = int(location.pm10value.text)

# print(dust)

if dust > 150:
    dust_rate = '매우나쁨'
elif 80 < dust <= 150:
    dust_rate = '나쁨'
elif 30 < dust <= 80:
    dust_rate = '보통'
else :
    dust_rate = '좋음'

print(dust_rate)