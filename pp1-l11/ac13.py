import random

class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)

    @staticmethod
    def print_in_row(array):
        for c in array:
            print(c, end=".")

    @staticmethod
    def create_array(number_of_array_elements, value_of_array_elements):
        list = []
        for i in range(number_of_array_elements):
            list.append(value_of_array_elements)
        return list

    @staticmethod
    def create_random_array(number_of_array_elements, value_from, value_to):
        list = []
        for i in range(number_of_array_elements):
            list.append(random.randint(value_from, value_to))
        return list

    @staticmethod
    def count_numbers_in_range(array, value_from, value_to):
        count = 0
        for i in array:
            if value_from <= i <= value_to:
                count += 1
        return count

array1 = Arrays.create_array(10, 4)
array2 = Arrays.create_random_array(20, -7, 8)
print(array1)
print(array2)
print(Arrays.count_numbers_in_range(array2, -1, 1))
