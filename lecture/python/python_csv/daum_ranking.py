import requests
import csv
from pprint import pprint
from bs4 import BeautifulSoup

daum_url = 'https://www.daum.net/'
response = requests.get(daum_url).text

data = BeautifulSoup(response, 'html.parser')
rankings = data.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol > li > div > div:nth-child(1) > span.txt_issue > a') # 여러개(리스트)
# data.select_one() # 한 개


# for idx, rank in enumerate(rankings, 1):
#     print(f'{idx}위 : {rank.text}')

# 데이터를 딕셔너리로 만들기
# result_dict = {}
# for idx, rank in enumerate(rankings, 1):
#     result_dict[f'{idx}위'] = rank.text
# print(result_dict)

# 위에서 만든 데이터로 csv에 저장
# with open('daum_rank.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     for item, rank in result_dict.items():
#         csv_writer.writerow([item, rank])

# 먼저 데이터를 json 데이터처럼 다시 만들기
result_list = []
for idx, rank in enumerate(rankings, 1):
    result_dict = {'rank': f'{idx}위', 'ranker': rank.text}
    result_list.append(result_dict)
# pprint(result_list)

# 새로 만든 데이터를 바탕으로 DictWriter 를 사용하기
with open('daum_rank.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # 저장할 데이터들의 필드 이름을 미리 지정(딕셔터리의 key 이름과 일치해야 함)
    fieldnames = ['rank', 'ranker']
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # 필드 이름을 csv 파일 최상단에 작성
    csv_writer.writeheader()
    # 리스트를 순회하며 key(csv의 필드)를 통해 value(내용)를 작성한다.ㄴ
    for item in result_list:
        csv_writer.writerow(item)