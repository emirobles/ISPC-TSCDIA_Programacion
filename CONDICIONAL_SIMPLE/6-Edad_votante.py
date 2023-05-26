#Realice un programa donde el usuario ingrese su edad. Si es mayor de
#16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.
#Desarrollado por Emilce Robles

print("EDAD VOTANTE\n")

print("-Se va a determinar si usted es apto para votar\n")

edad = int(input("Ingrese su edad: "))

if edad > 16:
    print("\nPuede votar!")
else:
    print("\nNo puede votar, tiene que esperar unos años para hacerlo.")