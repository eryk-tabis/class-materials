#TODO
key = input()
stack = []
while True:
    if key == "+":
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n1 + n2)
    elif key == "-":
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n1 - n2)
    elif key == "*":
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n1 * n2)
    elif key == "/":
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n1 / n2)
    elif key == "=":
        break
    else:
        stack.append(int(key))
    key = input()
print(stack.pop())