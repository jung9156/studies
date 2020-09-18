import os

#1. 작업할 위치로 이동
os.chdir(r'C:\Users\multicampus\Desktop\jungwon\startcamp\200116\dummy')

#2. 작업할 파일 목록 얻기
filenames = os.listdir('.')  #..은 뒤로가기, .은 현재 위치(1번에서 이미 이동 완료.)

#3. 파일 이름 바꾸기
# for filename in filenames:
#     os.rename(filename, f'SAMSUNG_{filename}')

#4.이름 수정하기.

print(filenames)

for filename in filenames:
    os.replace(filename, (f'SSAFY{filename[7:]}'))


