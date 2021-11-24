import sys


words = {} # {1:{'a': 2, 'b':3}}

for lines in sys.stdin:
    word = ''
    for c in lines:
        if 97 <= ord(c.lower()) <= 122:
            word += c.lower()
        else:
            if len(word) not in words:
                words[len(word)] = {}
            if word in words[len(word)]:
                words[len(word)][word] += 1
            else:
                words[len(word)][word] = 1
            word = ''

out = []
i = 1

while i <= max(words):
    temp = []
    if i in words:
        mx = 0
        for w in words[i]:
            if words[i][w] > mx:
                temp = []
                temp.append((w, words[i][w]))
                mx = words[i][w]
            elif words[i][w] == mx:
                temp.append((w, words[i][w]))
            
        out.append(sorted(temp))
    i += 1

for i in range(len(out)):
    print(f'length {len(out[i][0][0])}:', end=' ')
    for j in range(len(out[i])):
        occ = out[i][j][1]
        print(f'{out[i][j][0]}', end = ' ')

    if occ == 1:
        print(f'({occ} occurrence)')
    else:
        print(f'({occ} occurrences)')