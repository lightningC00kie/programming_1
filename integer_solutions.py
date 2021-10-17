solution = False
a = int(input())
b = int(input())

if b == 0:
    print(f'X = {a}, Y = {b}')
    print(f'X = {b}, Y = {a}')
    solution = True

i = 1
while i * i <= abs(b):
    if b % i == 0:
        z = b//i
        if i == z and a > 0 and i + z == a:
            print(f'X = {z}, Y = {i}')
            solution = True
        elif i == z and a < 0 and -i - z == a:
            print(f'X = {-z}, Y = {-i}')
            solution = True
        elif i + z == a:
            print(f'X = {z}, Y = {i}')
            print(f'X = {i}, Y = {z}')
            solution = True
        elif -i -z == a:
            print(f'X = {-z}, Y = {-i}')
            print(f'X = {-i}, Y = {-z}')
            solution = True
    i += 1

if solution == False:
    print('No solution')
