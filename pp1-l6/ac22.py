ar = [5, 1, 9, 6, 1]
for i in range(len(ar)):
    for j in range(len(ar) - 1):
        if ar[j] > ar[j + 1]:
            ar[j], ar[j + 1] = ar[j + 1], ar[j]
print(f"Array: {ar}\nResult: {ar[-1]-ar[0]}")
