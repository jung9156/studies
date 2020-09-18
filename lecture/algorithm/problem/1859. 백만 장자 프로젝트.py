import sys
sys.stdin = open("input.txt", "r")

tn = int(input())
for ir in range(tn):
    n = int(input())
    a = list(map(int, input().split()))
    M = 0
    st = 0
    i = 0
    k = a.index(max(a))
    while i != n:
        if i != k:
            M -= a[i]
            st += 1
            i += 1
        if i == k:
            M += a[i] * st
            st =0
            if i < n:
                i += 1
                if len(a[i:]) != 0:
                    k = a.index(max(a[i:]))
            else:


        #
        #
        #
        #
        if i < n:
            if i < k:
                M -= a[i]
                st += 1
            elif i == k:
                M = M + a[i] * st
                if len(a[i+1:]) != 0:
                    k = a.index(max(a[i+1:]))
                    st = 0



    print(M)