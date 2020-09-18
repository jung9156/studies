tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    A = input()
    mo = 'aeiou'
    for i in A:
        if i not in A:
            print(i, end='')
    print()