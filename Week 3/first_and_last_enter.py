s = str(input())
a1 = s.find('f')
a2 = s.rfind('f')
if a1 != a2:
    print(a1, a2)
else:
    print(a1)
