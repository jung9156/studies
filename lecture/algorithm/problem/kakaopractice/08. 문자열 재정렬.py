A = input()
re = 0
result = ""
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphbet = {}
for i in A:
    if i in alph:
        if i not in alphbet:
            alphbet[i] = 1
        else:
            alphbet[i] += 1
    else:
        re += int(i)
for i in alph:
    if i in alphbet.keys():
        result = result + (i * alphbet[i])
result = result + str(re)
print(result)