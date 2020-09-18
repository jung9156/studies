tn = int(input())
for ir in range(tn):
    print('#{}'.format(ir+1))
    N = int(input())
    word_d = [[] for i1 in range(51)]
    for i in range(N):
        w1 = input()
        word_d[len(w1)].append(w1)
    re = []
    for i2 in word_d:
        if i2:
            re += sorted(set(i2))
    for i in range(len(re)):
        print(re[i])

# 왜 제한시간 초과가 날까? 50/50 맞았는데???
# def di(k, x):
#     for i3 in range(len(x)-1):
#         di_n = i3
#         for i4 in range(i3+1, len(x)):
#             if alph[x[di_n][k]] >= alph[x[i4][k]]:
#                 if alph[x[di_n][k]] == alph[x[i4][k]]:
#                     k2 = k
#                     while True:
#                         k2 += 1
#                         if alph[x[di_n][k2]] != alph[x[i4][k2]]:
#                             break
#                     if alph[x[di_n][k2]] > alph[x[i4][k2]]:
#                         di_n = i4
#                 else:
#                     di_n = i4
#         x[di_n], x[i3] = x[i3], x[di_n]
#     for i in range(len(x)):
#         print(x[i])
# tn = int(input())
# result = []
# for ir in range(tn):
#     print('#{}'.format(ir + 1))
#     N = int(input())
#     word = []
#     word2 = [[] for i1 in range(51)]
#     alph = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
#     for i in range(N):
#         w1 = input()
#         word2[len(w1)].append(w1)
#     for ii in range(51):
#         if word2[ii]:
#             ww = set(word2[ii])
#             ww = list(ww)
#             word.append(ww)
#     for i2 in word:
#         di(0, i2)