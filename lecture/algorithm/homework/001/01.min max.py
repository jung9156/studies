test_case = int(input())

def Bubble(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

for i in range(test_case):
    answer = 0
    test_num = int(input())
    test_in = list(map(int, input().split()))
    result = Bubble(test_in)
    answer = result[-1]-result[0]
    print('#{} {}'.format(i+1, answer))
