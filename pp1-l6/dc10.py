def sum(array):
    sum = 0
    for i in array:
        sum += i
    return sum

def array2str(array):
    string = ""
    for i in array:
        string = string + str(i) + " "
    return string[0:len(string)-1]

ar = [4, 3, 7, 1, 3]
print(f"Array: {array2str(ar)}\nSum of values: {sum(ar)}")