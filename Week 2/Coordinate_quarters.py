x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# Определяем четверть первой точки
if x1 > 0:
    if y1 > 0:
        Q1 = 1
    else:
        Q1 = 4
elif x1 < 0:
    if y1 < 0:
        Q1 = 3
    else:
        Q1 = 2
# Определяем четверть второй точки
if x2 > 0:
    if y2 > 0:
        Q2 = 1
    else:
        Q2 = 4
elif x2 < 0:
    if y2 < 0:
        Q2 = 3
    else:
        Q2 = 2
# Сравниваем
if Q1 == Q2:
    print('YES')
else:
    print('NO')
