def fact(n):
    num_mul = 1
    for i in range(1, n + 1):
        num_mul *= i
        yield num_mul


for el in fact(5):
    print(el)
