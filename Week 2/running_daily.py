x, y = int(input()), int(input())
day = 1
while x < y:
    x = x + x * 0.1
    day += 1
print(day)
