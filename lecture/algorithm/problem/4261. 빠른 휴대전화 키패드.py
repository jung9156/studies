keypad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6':'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

tn = int(input())
for ir in range(tn):
    S, N = map(str, input().split())
    N = int(N)
    word = list(input().split())
    re = 0
    for i1 in range(len(word)):
        if len(word[i1]) == len(S):
            for i2 in range(len(word[i1])):
                if word[i1][i2] not in keypad[S[i2]]:
                    break
            else:
                re += 1
    print('#{} {}'.format(ir+1, re))