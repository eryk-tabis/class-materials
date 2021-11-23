from random import randint
with open("ac21.txt", "w") as file:
    for i in range(50):
        file.write(str(randint(100,999))+"\n")
