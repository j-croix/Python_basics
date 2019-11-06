s = str(input())
a1 = s.find('h')
a2 = s.rfind('h')
print(s[:a1] + s[a2 + 1:])
