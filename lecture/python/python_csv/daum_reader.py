import csv
with open('daum_rank.csv', 'r', encoding='utf-8', newline='') as csvfile:
    # print(csvfile)
    # fieldnames = ('rank', 'ranker')
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        print(row['rank'], row['ranker'])