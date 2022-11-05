def año():
    entero: int = int(input("escriba el año que quiere comprobar:"))
    if(entero % 4 == 0 and (entero % 100 != 0 or entero % 400 == 0)):
        print(f"El año {entero} es bisiesto")
    else:
        print(f"El año {entero} es bisiesto")
año()
