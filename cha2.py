def My_Role(name2,time,salary):
    try:
        if time > 40:
            heure_sup = time - 40
            salary = (salary * 40) + (heure_sup * salary * 1.5)
            return salary

        else:
            salary = time * salary
            return salary

    except ValueError:
        print("invalid number")

print(My_Role('saad',20,1200))
