name_file = input("Enter file name: ")
name_file = name_file + ".txt"
with open(name_file, 'r') as file:
    summary = 0
    for i in file:
        summary += 1
print(f"File name: {name_file}\nNumber of Lines: {summary}")
