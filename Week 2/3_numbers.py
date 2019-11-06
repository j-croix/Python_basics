a, b, c = int(input()), int(input()), int(input())
if a >= b and b > c:
    print(c, b, a)
elif a >= b and b <= c and a > c:
    print(b, c, a)
elif a >= b and b < c and a <= c:
    print(b, a, c)
elif a <= b and b > c and a < c:
    print(a, c, b)
elif a <= b and b > c and a >= c:
    print(c, a, b)
else:
    print(a, b, c)
