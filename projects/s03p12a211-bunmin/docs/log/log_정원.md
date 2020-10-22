# TIL_정원

### 0722

#### git

branch

merge

git clone -b branchname --single-branch 주소



#### 라즈베리파이

##### 시작

라즈비안을 SD카드를 통해 라즈베리에파이에 설치.
SHH오픈 후, 윈도우를 통해 제어 가능(PUTTY)



#### 파이 카메라

5초씩 잘라서 영상 저장 후, 다시 합쳐서 전송이 가능한가?





##### status의 경우 어떤 것을 넣을지에 대한 고민을 더 해보자.



##### SQL 공부중.



### 0723

#### 파이썬 파일 관리 공부

#### 영상 파일 처리 알고리즘 고민

-> 덮어쓰기가 가능한 덕분에 1~10번까지의 파일명 지정 후, 이벤트 시, 최근 6개 파일 합치는 방향으로 진행할 듯.

#### AWS서버 배포 관련해서 404error 처리를 위한 정보 수집.



### 0724

##### 파이썬 영상 처리 알고리즘(이라기엔 너무 허접하지만)

```python
A = list(range(0, 10))
N = 0
#N = (N + 1) % 10

#파일 선택
select_num = N
B = []
for _ in range(4, 10):
    title_num = (select_num + _) % 10
    #title_num 6번 반복
    B.append(title_num)
print(B)
```

->0부터 차례로 간다는 가정하에 파일 번호 리스트로 받는거

```python
A = list(range(0, 10))
N = 0
#N = (N + 1) % 10

#파일 선택
select_num = N
for i in range(10):
    B = []
    select_num = i
    for _ in range(4, 10):
        title_num = (select_num + _) % 10
        q = 'video' + str(title_num)
        #title_num 6번 반복
        B.append(q)
    print(B)
```

```python
['video4', 'video5', 'video6', 'video7', 'video8', 'video9']
['video5', 'video6', 'video7', 'video8', 'video9', 'video0']
['video6', 'video7', 'video8', 'video9', 'video0', 'video1']
['video7', 'video8', 'video9', 'video0', 'video1', 'video2']
['video8', 'video9', 'video0', 'video1', 'video2', 'video3']
['video9', 'video0', 'video1', 'video2', 'video3', 'video4']
['video0', 'video1', 'video2', 'video3', 'video4', 'video5']
['video1', 'video2', 'video3', 'video4', 'video5', 'video6']
['video2', 'video3', 'video4', 'video5', 'video6', 'video7']
['video3', 'video4', 'video5', 'video6', 'video7', 'video8']
```

10개의 파일일 경우 차라리 하드코딩으로 각 경우에 어떤 파일을 합칠지 정하는게 나을 것이라 예상



##### Dropbox 메뉴 도움

#### mysql 설치 및 공부

- 잘 모르겠음...



### 0727

#### IOT 서버 전송 공부

#### 프론트 드랍박스 공부



### 0728

#### .shell

```shell
cd/실행할 파일이 있는 주소/.py

sudo nano autostart          -파일 수정

lxterminal -e ~/실행할 파일.py
```

여기서 중요한 것은 다른 행동을 할 때에도 영상이 계속 저장되어야 한다는 점!

따라서 실행 파일을 두 개로 만드는 것이 나을 것이라 생각

1. 영상 저장
2. 버튼 눌렀을 때 저장된 영상 합치고, 서버에 전송(이름 편집 후)



#### 영상저장.py

```python
영상 저장
매 저장 Number를 number.txt에 저장하게 하자.
```

##### 영상 전송.py

```python
버튼이 눌리면 -> 그 순간의 number.txt를 가져온다.
해당 숫자에 맞는 영상 을 붙인 후에 전송(이름 편집)
```



##### 이름 편집 방법

- videos/블랙박스모델num/비디오저장날짜(?)