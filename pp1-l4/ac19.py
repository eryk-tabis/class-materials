def is_in_range(number, x, y):
    if number >= x and number <= y:
        return True
    else:
        return False


number = int(input("Enter number:"))
x = int(input("Enter first range:"))
y = int(input("Enter second range:"))
if is_in_range(number, x, y):
    print(f"Number {number} is in range")
else:
    print(f"Number {number} is not in range")