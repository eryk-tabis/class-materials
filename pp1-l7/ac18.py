with open("textfile.txt", "r") as file_open, open("copy.txt", "w") as file_write:
    file_write.write(file_open.read())

