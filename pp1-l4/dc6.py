def display_keypad():
    for i in range(1, 10):
        if i % 3 == 0:
            print(i)
        else:
            print(i, end=" ")


display_keypad()
