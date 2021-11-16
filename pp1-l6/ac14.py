ar = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
names = " ".join(ar)
max = len(ar[0])
l_name = ar[0]
for i in ar:
    if len(i) > max:
        max = len(i)
        l_name = i

print(f"Names: {names}\nLongest name: {l_name}")
