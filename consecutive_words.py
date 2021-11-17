import sys

words = {}
temp = ''
for line in sys.stdin:
    for c in line:
        if c.isalpha() and 65 <= ord(c.upper()) <= 90:
            temp += c
        else:
            if temp in words:
                words[temp] += 1
            else:
                words[temp] = 1
            temp = ''
if '' in words:
    del words['']

occurence = sorted(words.values())[::-1]
common = []

for j in occurence:
    for k in words:
        if words[k] == j:
            common.append((k, j))
            del words[k]
            break
    if len(common) == 20:
        break

[print(i, j) for i, j in common]