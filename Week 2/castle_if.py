a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
s = d * e
if (a <= d and a <= e) and (b <= d and b <= e):
    if (b <= d and b <= e) and (c <= d and c <= e):
        if (a <= d and a <= e) and (c <= d and c <= e):
            if a * b <= s or a * c <= s or b * c <= s:
                print('YES')
else:
    print('NO')
