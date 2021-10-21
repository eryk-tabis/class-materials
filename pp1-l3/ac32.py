string = ""
for x in range(1, 8):
    a = -7 + x
    for y in range(7):
        a += 7
        string += str(a)+" "
    print(string)
    string = ""
