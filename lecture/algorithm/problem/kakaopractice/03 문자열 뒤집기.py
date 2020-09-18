A = list(map(int, input()))
re = 0
fl = 0
a = A[0]
for i in A:
    if a != i:
        if fl == 0:
            re += 1
            a = i
            fl = 1
        elif fl == 1:
            fl -= 1
            a = i
print(re)
