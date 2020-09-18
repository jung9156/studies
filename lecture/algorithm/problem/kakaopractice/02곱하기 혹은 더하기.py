A = list(map(int, input()))
re = 0
for i in A:
    if re + i > re * i:
        re += i
    else:
        re *= i

print(re)