tn = int(input())
result = []
for ir in range(tn):
    A = list(input())
    rn = 0
    n = 0
    stack = []
    for i1 in range(len(A)):
        if A[i1] == '(':
            if A[i1 + 1] == ')':
                for i in range(len(stack)):
                    stack[i] += 1
            else:
                stack.append(0)
        else:
            if A[i1-1] == ')':
                n += stack.pop(-1) + 1
    result.append(n)
for re1 in range(tn):
    print('#{} {}'.format(re1+1, result[re1]))