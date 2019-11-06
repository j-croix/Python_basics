now = int(input())
seqSum = 0
count = 0
while now != 0:
    seqSum = seqSum + now
    count += 1
    now = int(input())
average = seqSum / count
print(average)
