import sys
inp = []
count = 0
for lines in sys.stdin:
    if lines.strip() == '0':
        break
    if count == 0:
        n = int(lines.strip())
    else:    
        inp.append(lines.strip().split())
    count += 1
inp = [[int(j) for j in i] for i in inp]

def count_row_zeroes(a):
    row_zeroes = []
    counter = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == 0:
                counter += 1
            else:
                row_zeroes.append(counter)
                counter = 0
        row_zeroes.append(counter)
        counter = 0
    return row_zeroes

def count_col_zeroes(a):
    col_zeroes = []
    counter = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[j][i] == 0:
                counter += 1
            else:
                col_zeroes.append(counter)
                counter = 0
        col_zeroes.append(counter)
        counter = 0 
    return col_zeroes

def solve(n,m,a):
    row = count_row_zeroes(a)
    col = count_col_zeroes(a)
    r_counter = 0
    c_counter = 0
    for i in range(len(row)):
        if row[i] >= n:
            r_counter += (1+row[i]-n)
    for i in range(len(col)):
        if col[i] >= n:
            c_counter += (1+col[i]-n)
    return r_counter, c_counter

a = []
sol = []
for i in range(len(inp)):
    if len(inp[i]) == 1:
        m = inp[i][0]
        for j in range(i+1, i+m+1):
            a.append(inp[j])
        sol.append(sum(solve(n,m,a)))
        a = []

for i in sol:
    print(i)
