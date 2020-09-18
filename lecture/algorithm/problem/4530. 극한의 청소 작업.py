def check(x, i1):
    global w
    x = int(x)
    if x < 5:
        return (x * cham[w - i1 -1])
    else:
        return ((x - 1) * cham[w - i1 -1] + (10 ** (w-i1)))


cham = [1]
s = 0
n = 1
while True:
    if n == 12:
        break
    s = (cham[-1] * (8)) + (10 ** n)
    cham.append(s+cham[-1])
    n += 1

tn = int(input())
for ir in range(tn):
    N_l = list(map(int, input().split()))
    mi_n = []
    mi_num = 0
    for ii in N_l:
        N3 = str(abs(ii))
        w = len(N3) - 1
        f_n = 0
        for i1 in range(w):
            f_n += check(N3[i1], i1)
        if int(N3[-1]) > 4:
            f_n += 1
        mi_n.append(f_n)
    number = []
    for i3 in range(2):
        number.append(abs(N_l[i3]) - mi_n[i3])
    if N_l[0] * N_l[1] < 0:
        print('#{} {}'.format(ir+1,number[0] + number[1] - 1))
    else:
        print('#{} {}'.format(ir+1, abs(number[1] - number[0])))