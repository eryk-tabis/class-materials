def minmax(array):
    array.sort()
    ar = [array[0], array[-1]]
    return ar
ar = [4, 2, 8, 4, 7, 7, 9, 5]
print(f"Array: {str(ar)}\nResult: {minmax(ar)}")
