quantity = 0
summary = 0
number = 0
while True:
    number = int(input("Enter number: "))
    if number == 0:
        break
    else:
        summary += number
        quantity += 1
print(f"RESULT: Quantity={quantity}, Sum={summary}, Mean={summary/quantity}")
