import sys

s = []
a = ''
out = []

for lines in sys.stdin:
    line = lines.strip()

    for c in line:
        s.append(c)
    
    if line[-1] != '.':
        s.append(' ')

for i in s:
    if a == '' and i == ' ':
        continue 
    else:
        a += i
    
    if i == '.':
        out.append(a)
        a = ''

for i in out:
    print(i)