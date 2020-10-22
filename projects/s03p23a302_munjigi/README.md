# [Sub PJT 2] 문지기 프로젝트

## Sub PJT 2 란?

- 빅데이터 프로젝트로 데이터 분석을 통한 빅데이터 추천 알고리즘을 구현하여 추천 웹 사이트를 목표로 한다.

### 대표적인 추천 시스템

- 컨텐츠 기반 필터링 (Content Based Filtering: CBF)
  - 추천의 대상이 되는 아이템과 사용자에 대한 이해를 바탕으로 추천하는 방식
- 협업 필터링(Collaborative Filtering: CF)
  - 사용자의 아이템에 대한 기록 정보를 바탕으로 특성 벡터를 직접 수치화하는 것이 아닌 머신러닝 방식으로 자동적으로 수치화함으로써 각 사용자가 무엇을 좋아할지 예측하는 기법



## :smiley: ​프로젝트 소개

### 기획 배경

- 기존 문화재 정책은 문화재 향유 및 문화재 활용 측면에서 부족한 현실
- 국민적 관심 제고를 위해 혁신적인 서비스로 국민의 관심과 참여 유도의 필요성
- 문화재 분야에 과학기술 및 ICT를 통한 새로운 가치 창출

### 프로젝트 이름

![로고](https://user-images.githubusercontent.com/60081201/92375343-f2608e00-f13b-11ea-9644-fcbb36c11497.png)



### 사용 언어, 기술 스택

<img src="https://img.shields.io/badge/backend-django-ff69b4" alt="기술스택" style="zoom:120%;" /><img src="https://img.shields.io/badge/frontend-Vue.js-green" alt="기술스택" style="zoom:120%;" /><img src="https://img.shields.io/badge/database-MySQL-yellowgreen" alt="기술스택" style="zoom:120%;" /><img src="https://img.shields.io/badge/server-AWS-9cf" alt="기술스택" style="zoom:120%;" /><img src="https://img.shields.io/badge/language-JavaScript, Python-important" alt="기술스택" style="zoom:120%;" />



### :key: ​프로젝트 사용법

로컬 웹 서버 실행 방법

#### Frontend

```bash
$ cd frontend/
$ npm install
# 서버를 실행합니다.
$ npm run serve
```

#### Backend

```bash
$ cd backend/
# 가상 환경을 켜줍니다.
$ python -m venv venv
$ source venv/Scripts/activate
# 필요한 설치파일을 다운 받습니다.
$ pip install -r requirements.txt
# 모델링 데이터 베이스에 등록합니다.
$ python manage.py makemigrations
$ python manage.py migrate
# 문화재 데이터를 등록합니다.
$ python manage.py loaddata tag.json
$ python manage.py loaddata heritage_videourl.json
# 서버를 실행합니다.
$ python manage.py runserver
```



## ERD

![erd](https://user-images.githubusercontent.com/60081201/93542918-3c940b80-f995-11ea-8a27-90a14c5b36f3.png)

- 문화재청에서 제공하는 API를 참고하여 작성한 ERD 입니다.



## 와이어 프레임

### 홈 페이지

- 메인 페이지로 문지기의 기능 소개와 인기 문화재 순위, 월별 행사 정보를 얻을 수 있도록 구성하였습니다.

![메인페이지](https://user-images.githubusercontent.com/60081201/93542917-3c940b80-f995-11ea-9c10-af04445ada53.png)

### 문화재 추천 페이지

- 문화재 추천 화면에서는 핵심 기능인 사용자 맞춤 문화재 추천 서비스를 제공하며 카로젤로 보여줄 예정입니다.
- 문화재 검색 기능을 갖고 인기 문화재를 무한 스크롤을 이용하여 제공할 것 입니다.

![문화재추천화면](https://user-images.githubusercontent.com/60081201/93542923-3e5dcf00-f995-11ea-935e-d1265904bf34.PNG)

### 문화재 디테일 페이지

- 문화재 카드를 클릭하게 되면 볼 수 있는 화면으로 관련 문화재에 대한 자세한 정보를 얻을 수 있습니다.
- 위치 정보뿐 아니라 문화재에 대한 리뷰 정보를 볼 수 있도록 구성하였습니다.

![디테일화면](https://user-images.githubusercontent.com/60081201/93542911-3aca4800-f995-11ea-874c-f12c6bb67851.PNG)

### 게시판 페이지

- 문화재 방문 리뷰를 볼 수 있는 화면으로 인기순과 최신순으로 선택하여 볼 수 있도록 제공할 것입니다.

![게시판](https://user-images.githubusercontent.com/60081201/93543248-0d31ce80-f996-11ea-9535-cfee5b63aa3c.PNG)

### 지도 페이지

- 카카오맵 API를 활용하여 지도정보를 제공합니다.
- 선택한 지역의 문화재들을 확인할 수 있고 그 주변 시설(편의점, 주유소 등) 정보를 제공합니다.

![지도](https://user-images.githubusercontent.com/60081201/93542935-4158bf80-f995-11ea-9367-5a0e6bd4ddba.PNG)

### 마이페이지

- 사용자의 찜한 문화재, 리뷰 작성한 게시글 목록을 확인할 수 있는 페이지입니다.
- 사용자의 프로필 설정이 가능하고 리뷰 작성 개수를 기준으로 등급을 주는 재미 요소를 기획하였습니다.
- 성씨를 입력하여 조상님 관련 문화재도 확인할 수 있도록 기획하였습니다.

![마이페이지](https://user-images.githubusercontent.com/60081201/93542914-3b62de80-f995-11ea-8fe3-5e5857b53bf4.PNG)



## :calendar: ​ 개발일정

![sub-pjt2일정](https://user-images.githubusercontent.com/60081201/93546038-e4610780-f99c-11ea-9185-75bb3b80c506.PNG)



## :school: 팀 소개

![esc](https://user-images.githubusercontent.com/60081201/93543792-7108c700-f997-11ea-9642-cb251ae73043.PNG)
