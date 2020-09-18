def ga(a, b, n):
    global cnt
    if b == n and a == n:
        cnt += 1
        return

    if b + 1 < N and A[a][b+1] == 0:
        ga(a, b+1, n)
    if a + 1 < N and b + 1 < N and A[a+1][b] == 0 and A[a][b+1] == 0 and A[a+1][b+1] == 0:
        dae(a+1, b+1, n)

def sae(a, b, n):
    global cnt
    if a == n and b == n:
        cnt += 1
        return
    if a + 1 < N and A[a+1][b] == 0:
        sae(a + 1, b, n)
    if a + 1 < N and b + 1 < N and A[a+1][b] == 0 and A[a][b+1] == 0 and A[a+1][b+1] == 0:
        dae(a+1, b+1, n)

def dae(a, b, n):
    global cnt
    if a == n and b == n:
        cnt += 1
        return

    if b + 1 < N and A[a][b+1] == 0:
        ga(a, b+1, n)
    if a + 1 < N and A[a+1][b] == 0:
        sae(a + 1, b, n)
    if a + 1 < N and b + 1 < N and A[a+1][b] == 0 and A[a][b+1] == 0 and A[a+1][b+1] == 0:
        dae(a+1, b+1, n)

