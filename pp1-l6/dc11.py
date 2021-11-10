def compare(array1, array2):
    if len(array1) == len(array2):
        for i in range(len(array1)):
            if array1[i] != array2[i]:
                break
        else:
            return True


array1 = ["water", "book", "sky"]
array2 = ["water", "book", "sky"]
print(compare(array1,array2))
array3 = [True, False]
array4 = [True, False, True]
print(compare(array3, array4))
array5 = [5, 3, 1]
array6 = [5, 3, 1]
print(compare(array5, array6))
array7 = [3, 2, 1]
array8 = [3, 2]
print(compare(array7, array8))
