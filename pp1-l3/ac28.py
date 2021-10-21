a = 0
b = 1
fib = 0
print(a)
print(b)
for x in range(2, 15):
    fib = a + b
    a = b
    b = fib
    print(fib)
