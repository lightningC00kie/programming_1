n = int(input())
_sum = 0
is_square = is_cube = False
for i in range(1, n):
    if i**2 == n:
        is_square = True
    if i**3 == n:
        is_cube = True
    if n % i == 0:
        _sum += i

result = ''



if _sum == n:
    result += 'P'
if is_square:
    result += 'S'
if is_cube:
    result += 'C'

print(result)