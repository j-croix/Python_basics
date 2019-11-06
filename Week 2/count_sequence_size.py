max_count = 0
count = 1
a = int(input())
previous = a
while a != 0:
    a = int(input())
    if a == previous:
        count += 1
    if a != previous:
        max_count = max(count, max_count)
        count = 1
    previous = a
print(max_count)
