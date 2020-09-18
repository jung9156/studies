def du(a, b):
    return a + b

def bba(a, b):
    return abs(a - b)

def gob(a, b):
    return a * b

def nanu(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'
