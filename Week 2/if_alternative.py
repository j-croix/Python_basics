a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if b <= a >= c:
    min1 = b
    min2 = c
elif a <= b >= c:
    min1 = a
    min2 = c
elif b <= c >= a:
    min1 = a
    min2 = b

if (min1 <= d and min2 <= e) or (min1 <= e and min2 <= d):
    print("YES")
else:
    print ("NO")
