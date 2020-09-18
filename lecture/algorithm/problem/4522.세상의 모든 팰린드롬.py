tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    A = list(input())

    for i in range(len(A)//2):
        if A[i] != A[-i -1]:
            if A[i] == '?' or A[-i -1] == '?':
                continue
            else:
                print('Not exist')
                break
    else:
        print('Exist')