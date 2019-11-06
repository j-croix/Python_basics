now = -1
max1 = 0
max2 = 0
a = list()
while now != 0:
    a.append(now)
    now = int(input())
a.sort(reverse=True)
print(a[1])
