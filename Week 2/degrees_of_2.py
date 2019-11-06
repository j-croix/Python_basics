n = int(input())
start = 1
print('1', end=' ')
while 2 * start <= n:
    print(2 * start, end=' ')
    start += start
