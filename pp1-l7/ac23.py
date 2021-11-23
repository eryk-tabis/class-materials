import csv
with open("students.txt", "r") as file:
    read = csv.reader(file, delimiter=',')
    next(read)
    for row in read:
        if int(row[2]) < 30:
            print(row[0], row[1], row[4])
