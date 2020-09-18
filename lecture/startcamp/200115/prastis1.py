import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com/marketindex/').text

data = BeautifulSoup(response,'html.parser')

exchange = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print('현재 원/달러 환율은 {}원'.format(exchange.text))

