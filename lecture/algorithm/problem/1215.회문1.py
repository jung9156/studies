# tn = int(input())
for ir in range(10):
    n = int(input())
    word = [input() for ii in range(8)]
    wl = []
    wl2 = []
    wn = len(word)
    cou = 0

    for iii in range(wn):
        wl2 = []
        for jjj in range(wn):
            wl2.append(word[iii][jjj])
        wl.append(wl2)
    for i in range(wn):
        for j in range(wn - (n-1)):
            check = wl[i][j:j+n]
            if check == check[::-1]:
                cou += 1

    for i2 in range(wn):
        for j2 in range(wn - (n-1)):
            check2 = []
            for j3 in range(n):
                check2 += wl[j2 + j3][i2]
            if check2 == check2[::-1]:
                cou += 1
    print('#{} {}'.format(ir+1, cou))