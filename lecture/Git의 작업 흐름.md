# Git의 작업 흐름

add 커밋할 목록에 추가

commit 커밋(creat a snapshot) 만들기

pust 현재까지의 역사(commits) 가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기



Working directory -> INDEX(staging area)커밋 준비 ->HEAD -> GitHub



꼭 add로 커밋할 목록을 추가한 후에 커밋을 추가할 것.





### Git 기본

$ git add helloworld.py  #git의 sub-command 중 하나

$ git commit -m #-로 시작하면 보통 쇼트네임 옵션

$ git config --global user.name "John" #--로 시작하면 보통 롱 네임 옵션



### Git bash

pwd - 현재 working directory 경로를 알수 있다.(~ => home directory이라는 뜻)

ls		 ->  현재 작업 경로의 파일 리스트를 볼 수 있다.

clear 		-> 프린트 된 내용 초기화(그냥 글 지우는 기능) -> ctrl + L

touch a.text 		 -> a.text를 만들어줌

rm. a.text 				 ->a.text삭제

mkdir (폴더명)		   -> 폴더 만들기

rm -r (폴더명)		 -> 폴더 삭제

cd /		 ->시스템 최 하단으로 이동(루트)

cd ~ 		-> 홈으로 이동

cd -			-> 바로 직전 위치로 이동





### Git에 내 정보 넣기

$ git config  --global user.name jung9156

$ git config  --global user.email jung9156@gmail.com



### Git 시작

git init				 ->git 초기화  (master)가 붙으면서 이 폴더가 Git의 관리를 받고 있음을 표시.

(관리할 폴더 최 상단에 한번만 지정할 것.)			.git		-> .은 숨김파일을 의미

#### git status				->git 상태 확인(항상 상태 확인 할 것!)

$ git commit -m "first commit"					->git commit

git log			->git의 기록 확인. 상단이 최근(Head(현재 시점)) ->: 이 생길 경우 Q를 누르면 나옴.

.gitignore		->숨김파일로 이그노어 파일을 만든 후, 이 안에 올리고 싶지 않은 파일을 입력하면 git에 등록X

git add . 			->현재 위치의 모든 파일을 add(stage area에)

```
git remote add origin https://github.com/jung9156/test.git
```

git remote -v 					->상태??

git push -u origin master



# TIL - 수업 외적인 공부(public) ->잘 하면 채용에 도움.

# lectures - 수업내용 정리(private)



# git init

# git add .

# git commit -m "commit message"

# git remote add origin<해당 github url>

# git remote -v :remote 된 주소 확인

# git push -u origin master



# 1. 반드시 commit 이후에 push할 필요 없다.

# 2. `git push -u origin master` 이후에 push 는 명령어가 그냥 `git push` 라고만 해도 된다.

#### (단, `git push origin master` 이렇게 하면 계속 같은 명령어를 사용해야 한다.)

# 3. 컴퓨터를 옮길 시, 자격 증명 관리에서 제거 해야함.(git hub)

# 4.clone -> 다시 init 안해도 됨.

# 5.clone의 경우 remote, origin다 안해도 됨.

# 6.이미 푸쉬된 경우(Clone) 또한 Pull을 해야함.

(파일이 생성되있는 경우는 Pull, 그 외에는 clone)

# "Talk is cheap, show me your code"

