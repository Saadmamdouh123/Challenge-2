try:
    N = int(input("Entrez un nombre entier positif : "))
    if N < 1:
        print("Veuillez entrer un nombre positif supérieur ou égal à 1.")
    else:
        somme = 0
        i = 1
        while i <= N:
            somme += i
            i += 1
        print(f"La somme de 1 à {N} est : {somme}")
except ValueError:
    print("Veuillez entrer un nombre entier valide.")
