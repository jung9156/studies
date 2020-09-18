import csv

lunch = {
    '양자강': '02-111-2222',
    '김밥카페': '02-333-4444',
    '순남시레기': '02-555-6666'
}

# 파일을 열어야 함.
# open() 내장함수로 해당 파일을 열고 파일 객체를 만든다.
with open('lunch.csv', 'w', newline='',encoding='utf-8') as csvfile:

    csv_writer = csv.writer(csvfile)
    for item, number in lunch.items():
        csv_writer.writerow([item, number])
        








# # print(csv_writer)
# csv_writer.writerow(['스팸', '햄'])
# csv_writer.writerow(['밥', '달걀'])
# csv_writer.writerow(['쌀밥', '계란'])    
# # 파일 조작이 끝나면 반드시 닫아야 한다.
# csvfile.close()
