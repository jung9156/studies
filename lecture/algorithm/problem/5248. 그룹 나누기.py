import sys

sys.stdin = open('input.txt')

for ir in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    group_l = [-1 for i in range(N + 1)]
    Group = []
    re = 0
    for i in range(0, M * 2, 2):#입력받은 쌍 순회하기
        q = [A[i], A[i+1]]
        p = []#빈 리스트 만들어서 그룹 합치기용
        for i1 in q:
            if group_l[i1] != -1 and i1 not in p:#이미 그룹에 들어간 친구일 경우, 그룹에서 빼서 모두 p에 넣기(이미 빠진 친구 접근 막기)
                p += Group[group_l[i1]]
                Group[group_l[i1]] = []
            elif group_l[i1] == -1:#그룹에 속하지 않았던 친구일 경우 p에 같이 추가해주기
                p.append(i1)
        for i3 in p:#p에 있는 친구들 모두 그룹 위치 표시하기 (group_l이 그 역할)
            group_l[i3] = re #중복되는게 있으나 문제는 없어 보임..
        Group.insert(re, p)
        re = len(Group) #다음 그룹을 위해 GROUP내의 생성될 그룹 위치를 re에 저장
    result = 0
    for i1 in Group:
        if i1:
            result += 1
    for i in range(1, N + 1):#그룹에 속하지 않은 개인 참여자 수 더하기
        if group_l[i] == -1:
            result += 1

    print('#{} {}'.format(ir + 1, result))





