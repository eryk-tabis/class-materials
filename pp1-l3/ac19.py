years = int(input("Enter the dog's age in human years: "))
dog_years = 0
if years <= 2:
    dog_years = years * 10.5
else:
    dog_years = 21 + (years - 2) * 4
print(f"The dog's age in dog’s years is {dog_years} years.")
