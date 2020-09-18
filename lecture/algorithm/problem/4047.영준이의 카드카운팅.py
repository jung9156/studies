tn = int(input())
for ir in range(tn):
    car = input()
    card = []
    card_n = len(car) // 3
    result = []
    ero = ''
    for i in range(card_n):
        k = car[3*i:3*(i+1)]
        card.append(k)
    # print(card)
    for i in range(len(card)):
        for ii in range(i+1, len(card)):
            if card[i] == card[ii]:

                ero += 'error'
    print('#{} '.format(ir + 1), end='')
    ca_di={'S': 13, 'D': 13, 'H': 13, 'C': 13}
    if ero != 'error':
        for i in range(card_n):
            ca_di[card[i][0]] -= 1

    else:
        print('ERROR')
        continue

    sdhc = 'SDHC'
    for i in sdhc:
        print(ca_di[i],end=' ')
    print()