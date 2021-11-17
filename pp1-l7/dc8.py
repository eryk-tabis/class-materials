with open('countries.txt', 'r') as file:
    index = 1
    for line in file:
        print(index, line, end=" ")
        index += 1