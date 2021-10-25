n = int(input("Enter number: "))
x = 0
z = 2
while x < n:
    y = 2
    while y <= z ** 1/2:
        if z % y == 0:
            break
        y += 1
    else:
        print(z)
        x += 1
    z += 1
