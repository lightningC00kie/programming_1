import sys

count = 0
inp = []
for line in sys.stdin:
    count += 1
    inp.append(line.split())
    
    if count == 2:
        break

def check_flood(l):
    for key in l:
        if l[key] > 1:
            return True

def warning():
    n, m= int(inp[0][0]), int(inp[0][1])
    f = [int(i) for i in inp[1]]
    lakes = {}
    dangerKeys = []
    drunk = []
    counter = 0
    drunk_ind = []
    for i in range(n):
        lakes[i+1] = 1

    for i in range(m):
        if f[i] != 0:
            dangerKeys.append(f[i])
        else:
            drunk.append(0)
    for i in range(m):
        if f[i] == 0:
            for j in range(i+1, m):
                if f[j] and lakes[f[j]] >= 1 and j not in drunk_ind:
                    lakes[f[j]] -= 1
                    drunk[counter] = f[j]
                    drunk_ind.append(j)
                    break
            counter += 1

        elif lakes[f[i]] != None:
            lakes[f[i]] += 1
            

        if check_flood(lakes):
            return 'FLOOD', None

        if len(dangerKeys) == 0:
            break

    return 'OK', drunk

status = warning()
print(status[0])
if status[1]:
    print(' '.join([str(i) for i in status[1]]))

