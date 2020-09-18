# 모델 작성 또는 변경 시 필수 3단계

### 1. models.py 작성

### 2. makemigrations

### 3. migrate



추가 명령어(옵션)

sqlmigrate

showmigrations



## 관리자 계정은 반드시 migrate 이후에 진행해야 한다.

- #### 관리자 계정도 db에 저장할 곳이 있어야하기 때문에 

- python manage.py createsuperuser



Article.objects.all()

Article.objects.get(pk=1)

Article(title="", content="")