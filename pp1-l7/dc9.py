with open('numbers.txt', 'r') as numbers:
    sum = 0
    for number in numbers:
        sum += int(number)
print(sum)
