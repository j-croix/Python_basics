number = int(input())
first = number // 100
second = int(((number - (number - (number - number % 10))) / 10) % 10)
last = number - ((number // 10) * 10)
print(first + second + last)
