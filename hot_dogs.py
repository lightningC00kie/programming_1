import sys

count = revenue = [0] * 5001
sm = mx = ind = 0

for line in sys.stdin:
    for i in line.split():
        count[int(i)] += 1

for i in range(len(count)-1, 0, -1):
    sm += count[i]
    if count[i] != 0:
        revenue[i] = sm * i
    if revenue[i] > mx:
        mx = revenue[i]
        ind = i
    elif revenue[i] == mx:
        ind = i

print(ind)
