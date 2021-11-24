number = int(input("Natural Number: "))
stack = []
while number / 2 != 0:
    stack.append(number % 2)
    number = number // 2
print("Binary number: ", end="")
for i in range(len(stack)):
    print(stack.pop(), end="")
