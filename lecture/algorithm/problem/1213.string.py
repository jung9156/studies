for ir in range(10):
    n = int(input())
    word = input()
    words = input()
    wn = len(word)
    cou = 0
    for idx in range(len(words)):
        if words[idx] == word[0]:
            if words[idx:idx+wn] == word:
                cou += 1

    print('#{} {}'.format(n, cou))