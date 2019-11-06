a = int(input())
b = int(input())
c = int(input())
s1 = 0
s2 = 0
if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    s1 = 1
if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
    s2 = 1
z = s1 + s2
if z == 2:
    print('YES')
else:
    print('NO')
