try:
    name2 = input('Enter your name :')
    time = int(input('how many hour did you worked :'))
    salary = float(input('your hour salary is :'))

    if time > 40:
            heure_sup = time - 40
            salary = (salary * 40) + (heure_sup * salary * 1.5)

    else:
            salary = time * salary
    

    print(salary)
    print(f"Hello {name2}  your total salary {salary}")

except ValueError:
    print("invalid number")

   