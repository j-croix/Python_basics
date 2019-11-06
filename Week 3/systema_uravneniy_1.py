a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
delta_general = a * d - c * b
if delta_general != 0:
    delta1 = d * e - f * b
    delta2 = a * f - c * e
    x = delta1 / delta_general
    y = delta2 / delta_general
    if x % 1 == 0 and y % 1 == 0:
        print(int(x), int(y))
    else:
        print(x, y)
