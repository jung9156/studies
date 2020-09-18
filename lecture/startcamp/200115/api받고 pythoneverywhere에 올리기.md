공공데이터 포털-가입



대기오염 뭐시기 검색 서비스 활용 머시기

일반키 받기



대기오염 머시기 설명서

인증키

url

오퍼레이션

요청 메시지 명세

f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey={api_key}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6'

key 앞에는 ? 로

다른 부분은 &



BeautifulSoup

으로 data 중에서 item 뽑아오기(리스트 형식으로 돌아옴.)

data.find_all("키워드")   -> 키워드가 들어간 정보 뽑아오기



location -> 강남구는 7번째 index

location = items[7]



station = location.stationname.text    ->		강남구의 stationname에 있는 text 뽑아오기 -> 강남구

(.은 자식 태그로 들어가는 방법)



-> 어제 배운데로 app.py에 추가해서 페이지로 나타내기 가능(import requests, import BeautifulSoup 해야함)



pythoneverywhere 가입(메일 인증(프로모션에 있을 가능성)

웹 -> 뭐 만들고 기존에 만든거랑 같게 폴더 만들고 템플릿 올리고

app.py내용 복붙-저장-웹에서 리로드-ㄱㄱ

