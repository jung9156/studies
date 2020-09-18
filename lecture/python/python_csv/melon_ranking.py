import requests
from bs4 import BeautifulSoup
import csv
melon_url = 'https://www.melon.com/chart/index.htm'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
# 1. 순위 / 가수 / 노래제목을 뽑아서 프린트

# 3. 2번에서 만든 데이터로 csv 작성
response = requests.get(melon_url, headers=headers).text
data = BeautifulSoup(response, 'html.parser')
# ranksongs = data.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
# ranksingers = data.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a:nth-child(1)')
songs = data.select('#lst50')
result_list = []

for song in songs:
    rank = song.select_one('td:nth-child(2) > div > span.rank')
    title = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
    artists = song.select('td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
# 2. 데이터 가공 (json 처럼 데이터 만들기)
    q = [artist.text for artist in artists]
    artist2 = ' '.join(q)
    item = {'rank': rank.text, 'title': title.text, 'artists': artist2}
    result_list.append(item)


# result_list = []
# for idx, rank in enumerate(ranksingers):
#     result_dict = {'rank': f'{idx+1}위', 'singer': rank.text, 'song': ranksongs[idx].text}
#     result_list.append(result_dict)

with open('melon_ranking.csv', 'w',newline='',encoding='utf-8') as csvfile:
    fieldnames = ['rank', 'title', 'artists']
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in result_list:
        csv_writer.writerow(item)