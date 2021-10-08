n = int(input())
count = 0

for i in range(1, n+1):
    cur = i
    is_good = True

    while i > 0:
        temp = i % 10
        i //= 10
        
        if temp == 0 or cur % temp != 0:
            is_good = False
            break

    if is_good:
        count += 1

print(count)

