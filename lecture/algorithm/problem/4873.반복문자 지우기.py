tn = int(input())
for ir in range(tn):
    a = list(input())
    print('#{} '.format(ir+1),end='')
    qq = 1
    stack = []

    for i1 in range(len(a)):
        v = a.pop(0)
        if len(stack) == 0:
            stack.append(v)
        else:
            if v == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(v)

    print(len(stack))