k = int(input())
s = input()
s = s.upper()
encrypted = ''

if k > 26 and k > 0:
    k = k % 26
elif k < 0 and -k > 26:
    k = -((-k)%26)

for c in s:
    if c.isalpha():
        if k + ord(c) > 90:
            ind = 65 + (k + ord(c)) - 90 -1
            encrypted += chr(ind)
        elif k + ord(c) < 65:
            ind = 90 - (-k - (ord(c) - 65)) +1
            encrypted += chr(ind)

        else:
            encrypted += chr(ord(c)+k)
    else:
        encrypted += c

print(encrypted)