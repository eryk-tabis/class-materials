def fractional(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return n * fractional(n-1)


x = 10
print(f"{x}! = {fractional(x)}")

def fractional(n):
    sum=1
    for i in range(1,n+1):
        sum = sum*i
    return sum