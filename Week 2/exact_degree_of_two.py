n = int(input())
if n == 1:
    print('YES')
start = 1
while 2 * start <= n:
    interim = 2 * start
    start += start
if interim == n:
    print('YES')
else:
    print('NO')
