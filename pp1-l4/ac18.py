def get_sum_of_digits(number):
    length = len(str(number))
    summary = 0
    while length >= 0:
        summary += int(number / (10**(length - 1)))
        number = int(number % (10**(length - 1)))
        length -= 1
    return summary


print(get_sum_of_digits(33))
