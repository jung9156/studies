tn = int(input())
for ir in range(tn):
    s11 = input()
    s22 = input()
    s1 = list(s11[::-1])
    s2 = list(s22[::-1])
    j = 0
    print('#{} '.format(ir+1),end='')
    while 0 <= j <= ((len(s2)+1)-len(s1)):
        n = 0
        if s1[n] != s2[j]:
            for i1 in range(len(s1)):
                if s1[n] == s2[j+i1]:
                    j += i1
                    break
            else:
                j += len(s1)
        else:
            for i2 in range(len(s1)):
                if s1[i2] != s2[j + i2]:
                    j += i2
                    break
            else:
                print(1)
                break
        if j >= len(s2)-(len(s1)+1):
            print(0)
            break

