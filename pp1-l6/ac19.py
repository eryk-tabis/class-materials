ar = [2, 3, 2, 5, 8, 1, 9, 8]
str_ar = ""
unique = ""
for i in range(len(ar)):
    str_ar += str(ar[i]) + " "
    for j in range(len(ar)):
        if ar[i] == ar[j] and i != j:
            break
    else:
        unique +=str(ar[i])+" "
print(f"Array: {str_ar}\nUnique elements: {unique}")
