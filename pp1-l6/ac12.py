ar = [15,  8, 31, 47, 2, 19]
ex_array = ""
rev_array = ""
for i in range(len(ar)):
    ex_array += " "+str(ar[i])
    rev_array += " "+str(ar[len(ar)-i-1])
print(f"existed array:{ex_array}\nreverse array:{rev_array}")