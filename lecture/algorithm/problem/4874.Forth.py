def cal(i, n1, n2):
    if i == '+':
        return n1 + n2
    elif i == '-':
        return n1 - n2
    elif i == '*':
        return n1 * n2
    else:
        return n1 // n2
tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    A = list(input().split(' '))
    ex = ['+', '-', '*', '/']
    stack = []
    for i in A:
        if i not in ex and i != '.':
            stack.append(int(i))
        elif i == '.':
            if len(stack) != 1:
                print('error')
                break
            else:
                print(stack[0])

        else:
            if len(stack) < 2:
                print('error')
                break
            else:
                n2 = stack.pop(-1)
                n1 = stack.pop(-1)
                stack.append(cal(i, n1, n2))