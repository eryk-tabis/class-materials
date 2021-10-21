pin_code = "0805"
user_pin_code = ""
for x in range(3):
    user_pin_code = input("Enter the PIN code: ")
    if user_pin_code == pin_code:
        print("Correct...")
        break
    else:
        print("Incorrect...")
else:
    print("Sorry, your payment card has been blocked.")
