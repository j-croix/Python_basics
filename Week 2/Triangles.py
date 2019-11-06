a = int(input())
b = int(input())
c = int(input())

max = 0
min1 = 0
min2 = 0

if a > b:
    if a > c:
        max = a
        min1 = b
        min2 = c
    else:
        max = c
        min1 = a
        min2 = b

elif c > b:
    max = c
    min1 = a
    min2 = b
else:
    max = b
    min1 = a
    min2 = c


if a + b <= c or a + c <= b or b + c <= a:
    print('impossible')
elif max * max == (min1 * min1 + min2 * min2):
    print('rectangular')
elif max * max < (min1 * min1 + min2 * min2):
    print('acute')
else:
    print('obtuse')
