def factorial(liv):
    fact = 1
    for i in range(1, liv + 1):
        fact*= i
    return fact
liv2 = int(input('enter a number'))
print(factorial(liv2))
    

