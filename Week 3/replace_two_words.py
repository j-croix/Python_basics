s = str(input())
n = s.find(' ')
print(s[n+1:] +' ' + s[:n])
