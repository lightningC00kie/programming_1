import sys

en_freq = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153,
           0.772, 4.025, 2.406, 6.749,  7.507, 1.929, 0.095, 5.987, 6.327, 9.056,
           2.758, 0.978, 2.360, 0.150,  1.974, 0.074]

cz_freq = [8.421, 0.822, 0.740, 3.475, 7.562, 0.084, 0.092, 1.356, 6.073, 1.433,
           2.894, 3.802, 2.446, 6.468, 6.695, 1.906, 0.001, 4.799, 5.212, 5.727,
           2.160, 5.344, 0.016, 0.027, 1.043, 1.503]

word = []
let = []
freq = [0] * 26


for line in sys.stdin:
    word += line.split()

for i in word:
    for c in i:
        if c.isalpha():
            let.append(c.upper())


def find_freq(letters):
    for i in range(26):
        count = 0
        cur = chr(ord('A')+i)
        for j in range(len(letters)):
            if cur == letters[j]:
                count += 1
        freq[i] = count

find_freq(let)

def chi(freq):
    en = 0
    cz = 0
    for i in range(26):
        en += ((freq[i]/len(let) - (en_freq[i]/100))**2)/en_freq[i] 
        cz += ((freq[i]/len(let) - (cz_freq[i]/100))**2)/cz_freq[i]
    print(f'Match with English: {en*100:.2f}')
    print(f'Match with Czech: {cz*100:.2f}')
    print('Text is in English') if en < cz else print('Text is in Czech')
    return 

chi(freq)