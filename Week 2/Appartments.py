x = int(input())
y = int(input())
n = 0
if x == 1:
    print('YES')
elif x == 2 and y != 2:
   print('NO')
else:
    n = (y % x + 1)
    if y - x == n:
        print('NO')
