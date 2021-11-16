def arrayToString(array):
    str_ar = ""
    for i in array:
        str_ar += str(i)+","
    return str_ar[0:len(str_ar)-1]

ar = [5,4,3,2,6,5]
print(f"Array: {ar}\nString: {arrayToString(ar)}")
