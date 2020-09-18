def partition(a, st, end):
    pivot = (st + end) // 2
    L = st
    R = end
    while L < R:
        while a[L] < a[pivot] and L < R:
            L += 1
        while a[R] >= a[pivot] and L < R:
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R

def qS(a, st, end):
    if st < end:
        p = partition(a, st, end)
        qS(a, st, p-1)
        qS(a, p+1, end)

a = [69, 10, 30, 2, 16, 8, 31, 22]
qS(a, 0, 7)
print(a)