def turn1(x):
    x1 = [x[0][:], x[1][:], x[2][:]]
    for i in range(3):
        x[0][i], x[i][2], x[2][i], x[i][0] = x1[2-i][0], x1[0][i], x1[2-i][2], x1[2][i]

def turn2(x):
    x1 = [x[0][:], x[1][:], x[2][:]]
    for i in range(3):
        x[0][i], x[i][2], x[2][i], x[i][0] = x1[i][2], x1[2][2-i], x1[i][0], x1[0][2-i]



def cross(x):
    global L
    if x == 'F+':
        U1 = [U[0][:], U[1][:], U[2][:]]
        U[2] = [L[2-i][2] for i in range(3)]
        for i1 in range(3):
            L[i1][2] = D[2][i1]
        D[2] = [R[2-i][0] for i in range(3)]
        for i2 in range(3):
            R[i2][0] = U1[2][i2]
        turn1(F)

    elif x == 'F-':
        U1 = [U[0][:], U[1][:], U[2][:]]
        U[2] = [R[i][0] for i in range(3)]
        for i2 in range(3):
            R[i2][0] = D[2][2-i2]
        D[2] = [L[i][2] for i in range(3)]
        for i1 in range(3):
            L[i1][2] = U1[2][2-i1]
        turn2(F)

    elif x == 'B+':
        U1 = [U[0][:], U[1][:], U[2][:]]
        U[0] = [R[i][2] for i in range(3)]
        for i2 in range(3):
            R[i2][2] = D[0][2 - i2]
        D[0] = [L[i][0] for i in range(3)]
        for i1 in range(3):
            L[i1][0] = U1[0][2 - i1]
        turn2(B)

    elif x == 'B-':
        U1 = [U[0][:], U[1][:], U[2][:]]
        U[0] = [L[2-i][0] for i in range(3)]
        for i1 in range(3):
            L[i1][0] = D[0][i1]
        D[0] = [R[2-i][2] for i in range(3)]
        for i2 in range(3):
            R[i2][2] = U1[0][i2]
        turn1(B)

    elif x == 'U+':
        F1 = [F[0][:], F[1][:], F[2][:]]
        F[0] = R[0][:]
        R[0] = [B[0][2-i] for i in range(3)]
        B[0] = [L[0][2-i] for i in range(3)]
        L[0] = F1[0][:]
        turn1(U)

    elif x == 'U-':
        F1 = [F[0][:], F[1][:], F[2][:]]
        F[0] = L[0][:]
        L[0] = [B[0][2-i] for i in range(3)]
        B[0] = [R[0][2-i] for i in range(3)]
        R[0] = F1[0][:]
        turn2(U)

    elif x == 'D+':
        F1 = [F[0][:], F[1][:], F[2][:]]
        F[2] = L[2][:]
        L[2] = [B[2][2-i] for i in range(3)]
        B[2] = [R[2][2-i] for i in range(3)]
        R[2] = F1[2][:]
        turn2(D)

    elif x == 'D-':
        F1 = [F[0][:], F[1][:], F[2][:]]
        F[2] = R[2][:]
        R[2] = [B[2][2-i] for i in range(3)]
        B[2] = [L[2][2-i] for i in range(3)]
        L[2] = F1[2][:]
        turn1(D)

    elif x == 'L+':
        U1 = [U[0][:], U[1][:], U[2][:]]
        for i1 in range(3):
            U[i1][0] = B[2-i1][0]
        for i2 in range(3):
            B[i2][0] = D[i2][0]
        for i3 in range(3):
            D[i3][0] = F[2-i3][0]
        for i4 in range(3):
            F[i4][0] = U1[i4][0]
        turn1(L)

    elif x == 'L-':
        U1 = [U[0][:], U[1][:], U[2][:]]
        for i1 in range(3):
            U[i1][0] = F[i1][0]
        for i2 in range(3):
            F[i2][0] = D[2-i2][0]
        for i3 in range(3):
            D[i3][0] = B[i3][0]
        for i4 in range(3):
            B[i4][0] = U1[2-i4][0]
        turn2(L)

    elif x == 'R+':
        U1 = [U[0][:], U[1][:], U[2][:]]
        for i1 in range(3):
            U[i1][2] = F[i1][2]
        for i2 in range(3):
            F[i2][2] = D[2-i2][2]
        for i3 in range(3):
            D[i3][2] = B[i3][2]
        for i4 in range(3):
            B[i4][2] = U1[2-i4][2]
        turn1(R)

    else:
        U1 = [U[0][:], U[1][:], U[2][:]]
        for i1 in range(3):
            U[i1][2] = B[2-i1][2]
        for i2 in range(3):
            B[i2][2] = D[i2][2]
        for i3 in range(3):
            D[i3][2] = F[2-i3][2]
        for i4 in range(3):
            F[i4][2] = U1[i4][2]
        turn2(R)


tn = int(input())
for ir in range(tn):
    N = int(input())
    order = list(input().split())
    U = [list('w' for i1 in range(3)) for i2 in range(3)]
    D = [list('y' for i1 in range(3)) for i2 in range(3)]
    L = [list('g' for i1 in range(3)) for i2 in range(3)]
    R = [list('b' for i1 in range(3)) for i2 in range(3)]
    F = [list('r' for i1 in range(3)) for i2 in range(3)]
    B = [list('o' for i1 in range(3)) for i2 in range(3)]
    for i in range(N):
        cross(order[i])

    for i in range(3):
        print(''.join(U[i]))