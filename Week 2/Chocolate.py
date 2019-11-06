n, m, k = int(input()), int(input()), int(input())
if k > m * n or k == 0 or m == 0 or n == 0:
    print('NO')
elif k % n == 0 or k % m == 0:
    print('YES')
elif k % n != 0 or k % m != 0:
    print('NO')
