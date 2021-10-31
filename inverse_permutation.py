l = input().split()
n = int(l.pop(0))
inv = [0] * len(l)

for i in range(len(l)):
    inv[int(l[i])-1] = str(i + 1)

print(' '.join(inv))