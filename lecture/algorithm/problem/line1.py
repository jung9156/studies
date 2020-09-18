inputString = '({[<>]}'


def solution(inputString):
    answer = -1
    A = list(inputString)
    open = ['(', '{', '[', '<']
    close = [')', '}', ']', '>']
    stack = []
    re = 0
    for i in A:
        if i in open:
            stack.append(i)
        elif i in close:
            if stack:
                i_num = close.index(i)
                if open[i_num] == stack[-1]:
                    re += 1
                    stack.pop(-1)
                else:
                    return answer
            else:
                return answer
    else:
        if stack:
            return answer
        else:
            answer = re



    return answer

print(solution(inputString))