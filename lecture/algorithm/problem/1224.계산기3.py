def cal(n1, n2, x):
    if x == '+':
        return n1 + n2
    elif x == '-':
        return n1- n2
    elif x == '*':
        return n1 * n2
    else:
        return n1 // n2
tn = 1
for ir in range(10):

    N = int(input())
    A = input()
    ex = '+-/*()'
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}

    stack = []
    susik = []
    for i in A:

        if i not in ex:
            susik.append(int(i))
        else:
            if i == ')':
                while True:
                    c = stack.pop(-1)
                    if c == '(':
                        break
                    susik.append(c)

            else:
                if len(stack) == 0:
                    stack.append(i)
                    continue
                else:
                    if icp[i] <= isp[stack[-1]]:
                        while icp[i] <= isp[stack[-1]]:
                            susik.append(stack.pop(-1))
                        stack.append(i)
                    else:
                        stack.append(i)

    stack = []

    for i in susik:
        if str(i) not in ex:
            stack.append(i)
        else:
            n1, n2 = stack.pop(-2), stack.pop(-1)
            stack.append(cal(n1, n2, i))
    print('#{} '.format(tn),end='')
    print(*stack)
    tn += 1