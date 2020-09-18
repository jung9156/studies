def solution(w,h):
    if w > h:
        h, w = w, h
    h1, w1 = h, w
    answer = 1
    while True:
        if h1 % w1 == 0:
            break
        else:
            h1, w1 = w1, h1 % w1

    answer = h * w - (h + w - w1)

    return answer