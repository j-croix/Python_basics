import math
a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4 * a * c
if a == 0:
    x = -c / b
    print(x)
elif d > 0:
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    if x1 % 1 == 0 and x2 % 1 == 0:
        print((min((int(x1), int(x2)))), max((int(x1), int(x2))))
    else:
        print(x1, x2)
elif d == 0:
    x = -b / (2 * a)
    print(x)
