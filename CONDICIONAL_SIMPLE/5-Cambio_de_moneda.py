#Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo
#el cambio de dólares a pesos y que sea el usuario quién decida qué tipo
#de cambio quiere, si de dólares a pesos o viceversa.
#Desarrollado por Emilce Robles

print("CAMBIO DE MONEDA\n")

print("-Solo admite dólares y pesos argentinos\n")

moneda = input("Ingrese la letra 'd' si quiere cambiar dolares o la letra 'p' si quiere cambiar pesos:")
cotización = float(input("Ingrese monto de contización (Equivalente de 1 USD en ARS):")) 

if moneda.lower() == "d":
    a = float(input("\nPor favor ingrese la cantidad de dolares a cambiar:"))
    cambio = a * cotización
    print("Para los", a, "USD ingresados le corresponden:", cambio, "ARS")
elif moneda.lower() == "p":
    b = float(input("\nPor favor ingrese la cantidad de pesos a cambiar:"))
    cambio = round((b / cotización), 2)
    print("Para los", b, "ARS ingresados le corresponden:", cambio, "USD")
else:
    print("\nLa moneda ingresada no corresponde a USD o ARS")