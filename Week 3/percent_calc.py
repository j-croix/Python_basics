p = int(input())
x = int(input())
y = int(input())
money = x * 100 + y
procent = float(1 + p / 100)
money_final = money * procent
print(int(money_final // 100), int((money_final % 100)))
