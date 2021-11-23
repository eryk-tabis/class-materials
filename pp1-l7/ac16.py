with open("textfile.txt","r") as file:
    f = 0
    for i in file:
        print(i, end='')
        if f == 4:
            if input("Press Enter to continue") == '':
                f = 0
                continue
            else:
                break
        f += 1
