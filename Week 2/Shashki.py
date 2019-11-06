h1, v1 = int(input()), int(input())
h2, v2 = int(input()), int(input())
p1 = h1 + v1
p2 = h2 + p2
if (p1) % 2 != 0 and (p2) % 2 == 0 or (p1) % 2 == 0 and (p2) % 2 != 0:
    print('NO')
elif v2 <= v1:
    print('NO')
elif (h2 - h1) < (v2 - v2):
    print('NO')
else:
    print('YES')
