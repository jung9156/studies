nosun = int(input())
for i in range(nosun):

    k_n_m = list(map(int, input().split()))
    k = k_n_m[0]
    n = k_n_m[1]
    m = k_n_m[2]
    l = k
    choong = list(map(int, input().split()))
    bustop = [0 for i in range(0, n+1)]
    result = 0
    gojang = []
    for jj in range(m):
        gojang.append(choong[jj] - choong[jj-1])
    if max(gojang) > k:
        result = 0
    else:
        for j in range(m):
            bustop[choong[j]] += 1

        while l < n:

            if bustop[l] == 1:
                bustop[l] -= 1
                l += k
            else:
                while bustop[l] == 0:
                    l -= 1
                bustop[l] -= 1
                l += k
            if l == 0:
                result = 0
                break
            else:
                result = m - bustop.count(1)





    print('#{} {}'.format(i+1, result))