def median(array):
    array.sort()
    if len(array) % 2 == 0:
        return (array[len(array/2)]+array[(len((array/2))+1)])/2
    else:
        return array[len(array)//2]
    
ar1 = [1, 0, 9, 4, 6]
ar2 = [6, 8, 3, 1, 0, 5, 7]
print(median(ar1))
print(median(ar2))