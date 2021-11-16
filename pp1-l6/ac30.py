import random
def rand_elem(array):
    return array[random.randint(0,len(array)-1)]

ar = [2,3,4,6,7,8]
print(rand_elem(ar))
