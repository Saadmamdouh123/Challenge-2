# def factorial(liv):
#     fact = 1
#     for i in range(1, liv + 1):
#         fact*= i
#     return fact
# liv2 = int(input('enter a number'))
# print(factorial(liv2))
#######################
# def NumEnt(m):
#     counter = 1
#     while counter <= 10:
#        result = counter * m 
#        counter += 1
#        print(result)

# live = int(input('enter a number '))
# print(NumEnt(live))
#######################
import math

def CarreParfait():
    try:
        n = int(input('Entrez un nombre entier : '))
        racine = math.sqrt(n)
        if racine.is_integer():
            print(n, 'est un carré parfait')
        else:
            print(n, 'n\'est pas un carré parfait')
    except ValueError:
        print("Veuillez entrer un entier valide.")

CarreParfait()




    

