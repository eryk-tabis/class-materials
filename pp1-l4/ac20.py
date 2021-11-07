def power(x, n):
    if n == 0:
        return x
    else:
        return x * pow(x, n-1)


print(power(2, 3))
