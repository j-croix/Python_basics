now = -1
equal = now
count = 0
count1, count2 = 0, 0
while now != 0:
    if now == equal:
        count1 += 1
    if now != equal:
        equal = now
        count2 = 1
    count = max(count1, count2)
    now = int(input())
print(count)
