ar = [3, 2, 6, 7, 8]
even = []
odd = []
for i in ar:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even+odd)
