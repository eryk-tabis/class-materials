ar1 = [4, 36, 12, 28, 9, 44, 5]
ar2 = [5, 1, 36]
for i in ar1:
    for j in ar2:
        if i == j:
            break
    else:
        print(i, end=" ")
