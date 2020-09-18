w, h = list(map(int, input().split()))
x, y = list(map(int, input().split()))
t = int(input())
x = (t + x)%(2*w)
y = (t + y)%(2*h)

x3 = x % (w)
y3 = y % (w)
if x > w:
    x = 2*w - x
if y > h:
    y = 2*h - y

print(x, y)