with open("textfile.txt", "r") as file_open, open("copy.txt", "w") as file_write:
    for i in file_open:
        file_write.write(i)

