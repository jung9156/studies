def solution(s):
    q = (len(s) // 2) + 1
    result = s
    for i in range(1, q):
        A = []
        re = ""
        for i2 in range(0, len(s), i):
            A.append(s[i2:i2 + i])
        r = 0
        stack = ''
        for i3 in A:
            if stack != i3:
                if r != 1:
                    stack = str(r) + stack
                re = re + stack
                stack = i3
                r = 1
            elif stack == i3:
                r += 1
        else:
            if r == 1:
                re = re + stack
            else:
                re = re + str(r) + stack
        if len(result) > len(re) - 1:
            result = re[1:]

    answer = len(result)

    return answer