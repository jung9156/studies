re = []
N = int(input())
A = list(map(int, input().split()))

A.sort()
a = 1
for i in A:
    if i > a:
        print(a)
        break
    else:
        a += i

#완탐..

# for n in range(1, len(A) + 1):
#     for i in itertools.combinations(A, n):
#         re.append(sum(i))
#
# for i in range(1, sum(A) + 1):
#     if i not in re:
#         print(i)
#         break