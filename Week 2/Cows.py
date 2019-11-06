n = int(input())
b = n - ((n // 10) * 10)
if 10 <= n <= 20:
    print(n, 'korov')
elif b == 0 or 5 <= b <= 9:
    print(n, 'korov')
elif n == 1 or b == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')
