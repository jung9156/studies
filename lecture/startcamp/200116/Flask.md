1. # variable routing

- 요청 주소의 특정 부분이 계속 바뀌어야 할 상황에서는 어떻게 해야 할까?

# 파이썬 파일 단 하나를 실행함으로써 서버가 켜진다!!!

- flask 는 기본적으로 `app.py` 를 서버파일로 알고 있다.

  - `app.py`가 아닌 다른 이름의 파일이라면 `'$ set FLASK_APP=hello.py'`

  - 단, `flask.py`는 사용할 수 없다.

# variable routing + render_template

## -> html 파일에 jinja2 사용



# jinja2 template

- flask 에 내장된 템플릿 엔진

- HTML 은 프로그래밍 언어가 아니기 때문에 조건문과 반복문을 사용할 수 없어서 도입된 엔진

  - 주의! {% 유저에게 보여지지 않는 부분%}

  - 주의! {{유저에게 보여지는 부분}}

# vonvon 신이 나를 만들때 clone coding

1. 이름 받는 페이지
2. 결과 보여줄 페이지
3. 이름 받을 페이지 보여줄 함수1
4. 결과 페이지 보여줄 함수2