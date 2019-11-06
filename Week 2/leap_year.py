a = int(input())
if a % 4 == 0 and not a % 100 == 0:
    print('Yes')
elif a % 400 == 0:
    print('YES')
else:
    print('NO')
