ar = [2, 3, 4, 5, 6]
even = 0
odd = 0
for i in ar:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Number of even numbers: {even}, number of odd numbers: {odd}")
