a = 4
b = 15
for x in range(a):
    if x == 0 or x == a - 1:
        print("*" * b)
    else:
        print("*" + " "*(b - 2) + "*")
