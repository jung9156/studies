tn = int(input())
for ir in range(tn):
    n1, n = list(input().split())
    a = list(input().split())
    che = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    result = [0 for i0 in range(10)]
    print(n1)
    for idx, val in enumerate(che):
        result[idx] = a.count(val)
    # print(result)
    for idx2, val2 in enumerate(result):
        for total in range(val2):
            print(che[idx2],end=' ')
    print()