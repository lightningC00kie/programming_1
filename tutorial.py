def no_zero(n):
    if n % 10 or n == 0:
        return(n)

    return no_zero(n//10)

def power(n):
    print(n)
    if n == 1:
        return True
    if n % 2 == 1 or n == 0:
        return False

    return power(n//2)

def sm(a, i, j):
    print(f'i = {i}, j = {j}')
    if i == j:
        return 0

    return a[i] + sm(a, i+1, j)
    
# sm([1,2,3,4], 0, 4)
# if --> False
# return 1 + sm(a, 1, 4)
# if --> False
# return 2 + sm(a, 2, 4)
# if --> False
# return 3 + sm(a, 3, 4)
# if --> False
# return 4 + sm(a, 4, 4)
# if --> True
# return 0

def recursive_max(a,i,j):
    if i == j - 1:
        return a[i]

    m = recursive_max(a, i + 1, j)

    return a[i] if a[i] > m else m