import json
from konlpy.tag import Kkma
from konlpy.tag import Hannanum
from konlpy.tag import Komoran
from konlpy.tag import Mecab
from konlpy.tag import Okt


okt = Okt()
mecab = Mecab()
komoran = Komoran
hannanum = Hannanum()
kkma = Kkma()
# print(kkma.nouns(u'대학에서 DB, 통계학, 이산수학 등을 배웠지만...'))



with open('heritage_data1.json', encoding='UTF8') as json_file:
    json_data = json.load(json_file)
# print(type(json_data))
a = []
for i in json_data:
    a.append(i)
for i in a:
    print(hannanum.nouns(json_data[i]["content"]))
    # print(kkma.nouns(json_data[i]["content"]))
    # print(komoran.nouns(json_data[i]["content"]))
    # print(mecab.nouns(json_data[i]["content"]))
    # print(okt.nouns(json_data[i]["content"]))

