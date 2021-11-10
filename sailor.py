import sys

count = 0
inp = []
for line in sys.stdin:
    count += 1
    inp.append(line.split())
    
    if count == 2:
        break

n = int(inp[0][0])
k = int(inp[0][1])

x = int(inp[1][0])
y = int(inp[1][1])

def find_adjacent(x, y, n):
    down = up = left = right = True
    if x + 1 >= n:
        right = False
    if y + 1 >= n:
        down = False
    if x - 1 < 0:
        left = False
    if y - 1 < 0:
        up = False
    return [up, down, right, left]

m = [[0 for i in range(n)] for j in range(n)]
m[x-1][y-1] = 1
cur = []

for t in range(k):
    cur = []
    for i in range(n):
        for j in range(n):
            if m[i][j] != 0:
                cur.append((i,j))
    
    for i in range(len(cur)):
        x, y = cur[i]
 
        adj = [up, down, right, left] = find_adjacent(x, y, n)
        if sum(adj) != 0:
            prob = (sum(adj)/4)/sum(adj)
        if up:
            m[x][y-1] += (m[x][y]*prob)
        if down:
            m[x][y+1] += (m[x][y]*prob)
        if right:
            m[x+1][y] += (m[x][y]*prob)
        if left:
            m[x-1][y] += (m[x][y]*prob)
        m[x][y] = 0

sm = 0
for i in m:
    sm += sum(i)

print(f'{sm:.3f}')

