n = int(input("Enter number: "))
for x in range(2, n+1):
    y = 2
    while y <= x**0.5:
        if x % y == 0:
            break
        y += 1
    else:
        print(x)
