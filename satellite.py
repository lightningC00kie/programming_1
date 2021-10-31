import sys

m = []
res = []
count = -1
plat = False

for line in sys.stdin:
    if float(line) < 0:
        break
    m.append(float(line))
    count += 1
    if len(m) == 3:
        if m[0] < m[1] and m[2] < m[1]:
            res.append(f'distance {count-1} height {m[1]:.1f}')
            m.pop(0)
        elif m[0] < m[1] and m[1] == m[2]:
            temp = [count, m[1]]
            plat = True
        else:
            m.pop(0)

    elif plat:
        if m[-1] != temp[1]:
            if m[-1] < temp[1]:
                res.append(f'distance {temp[0]-1} height {temp[1]:.1f}')
                m = m[-2:]
            elif m[-1] > temp[1]:
                plat = False
                m = m[-2:]
            else:
                continue

for l in res:
    print(l)