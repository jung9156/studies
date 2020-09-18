for ir in range(10):
    n = int(input())
    a = [list(map(int, input().split()))for iii in range(100)]
    a2 = a[0]
    st = []
    for idx, i10 in enumerate(a2):
        if i10 == 1:
            st.insert(0, idx)

    re = []
    result = 1000
    for i9 in st:
        j = i9
        cou = 0
        i = 1
        while True:
            if i == 99:

                if result > cou:
                    re = []
                    result = cou
                    re.append(i9)
                break
            if j-1 >= 0 and a[i][j-1] == 1:
                while True:
                    j -= 1
                    cou += 1
                    if j <= -1 or a[i][j] == 0:
                        j += 1
                        cou -= 1
                        break

            elif j+1 <= 99 and a[i][j+1] == 1:
                while True:
                    j += 1
                    cou += 1
                    if j >= 100 or a[i][j] == 0:
                        j -= 1
                        cou -= 1
                        break

            i += 1
            cou += 1

    kk = re[0]
    print('#{} {}'.format(n, kk))