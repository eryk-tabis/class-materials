ar = [1,23,5,382,1,17,4,906]
middle = "|"
for i in ar:
    middle += " "*(4-len(str(i)))+str(i)+"|"
print("-"*len(middle))
print(middle)
print("-"*len(middle))
