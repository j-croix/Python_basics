s = str(input())
a1 = s.find('f')
a2 = s.find('f', a1 + 1)
if a1 == -1:
    print('-2')
elif a2 == -1:
    print('-1')
else:
    print(a2)
