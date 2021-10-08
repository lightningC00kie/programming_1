y = int(input())
z = int(input())
days = 0
for i in range(y, z+1):
    if (i % 4 == 0 and i % 100 != 0) or (i % 4 == 0 and i % 100 == 0 and i % 400 ==0):
        days += 366
    else:
        days += 365

print(days)