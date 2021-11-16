ar1 = [2,3,4,8]
ar2 = [2,3,4,5,6,7]
for i in ar1:
    f = 0
    for j in ar2:
        if i == j:
            f = 1
    if f == 0:
        print("First array is not a subset of the second one")
        break
else:
    print("First array is a subset of the second one")
