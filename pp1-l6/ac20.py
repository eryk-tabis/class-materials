def occurs(number, array):
    for i in array:
        if number == i:
            return True
number = int(input("Number: "))
ar = [15, 38, 7, 23, 14]
str_ar = ""
for i in ar:
    str_ar += str(i)+" "
print(f"Array:{str_ar}")
if occurs(number, ar):
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appear in the array")
