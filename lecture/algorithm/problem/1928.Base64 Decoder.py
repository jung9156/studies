def ch_tw(x):
    numnum = ''
    while x != 0:
        if x % 2 == 0:
            numnum += '0'
            x = x // 2
        else:
            numnum += '1'
            x = x // 2
    while len(numnum) < 6:
        numnum += '0'
    return numnum[::-1]


pyo1 = list(range(0, 64))
pyo2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
pyo = {}
lastresult = []

for i, j in enumerate(pyo2):
    pyo[j] = pyo1[i]

change = []
bin_list = []
bin_result = ''
test_case = int(input())
test_word = ''
result2 = []
for i in range(test_case):

    test_word = ''.join(input())

    for i in test_word:
        bin_list.append(ch_tw(pyo[i]))
    bin_result = ''.join(bin_list)

    result = ''
    for i in range(0, len(bin_result), 8):
        result += chr(int(bin_result[i:i + 8], 2))

    lastresult.append(result)
    result = ''
    bin_result = ''
    bin_list = []
for i in range(test_case):
    print('#{} {}'.format(i + 1, lastresult[i]))
