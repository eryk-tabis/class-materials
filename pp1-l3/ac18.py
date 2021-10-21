amount_of_coin_5 = 0
amount_of_coin_2 = 0
amount_of_coin_1 = 0
amount_of_zloty = int(input("Enter the amount in PLN: "))
zloty = amount_of_zloty
while amount_of_zloty > 0:
    if amount_of_zloty - 5 >= 0:
        amount_of_coin_5 += 1
        amount_of_zloty -= 5
    elif amount_of_zloty - 2 >= 0:
        amount_of_coin_2 += 1
        amount_of_zloty -= 2
    else:
        amount_of_coin_1 += 1
        amount_of_zloty -= 1
print(f"The amount of PLN {zloty} in coins:\n 5 zł - {amount_of_coin_5} \n 2 zł - {amount_of_coin_2} \n 1 zł - {amount_of_coin_1}")
