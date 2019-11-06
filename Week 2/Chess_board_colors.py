A1 = int(input())
B1 = int(input())
A2 = int(input())
B2 = int(input())
if (A1 + B1) % 2 == 0 and (A2 + B2) % 2 == 0 or (A1 + B1) % 2 != 0 and (A2 + B2) % 2 != 0:
    print('YES');
else:
    print('NO')
