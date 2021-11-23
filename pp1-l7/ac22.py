with open("ac22.txt", "w") as file:
    for i in range(1, 11):
        string = ""
        for j in range(1, 4):
            string += str(i**j)+","
        file.write(string[:len(string)-1] + "\n")
