with open("shopping.txt", "a") as file:
    while True:
        product = input("Enter a product ('end' to stop)")
        if product == "end":
            break
        else:
            file.write(product + "\n")
