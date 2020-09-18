tn = int(input())
for ir in range(tn):
    a = list(input())
    stack = []
    qq = 0
    print('#{} '.format(ir + 1), end='')
    while len(a) > 0:
        i1 = a.pop(0)
        if i1 == '(' or i1 == '{':
            stack.append(i1)
        if i1 == ')' or i1 == '}':
            if len(stack) < 1:
                qq = 1
                print(0)
                break

            if i1 == ')':
                k1 = stack.pop(-1)
                if k1 != '(':
                    qq = 1
                    print(0)
                    break
            elif i1 == '}':
                k1 = stack.pop(-1)
                if k1 != '{':
                    qq = 1
                    print(0)
                    break
    if qq != 1:
        if len(stack) == 0:
            print(1)
        else:
            print(0)