n = int(input())
start = 1
if n == 1:
    print(0)
else:
    while 2 * start <= n:
        start += 1
print(start)
