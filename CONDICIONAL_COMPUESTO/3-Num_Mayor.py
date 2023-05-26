#Realice un programa que lea tres números, muestre cuál es el mayor y
#determine si es par o impar.
#Desarrollado por Emilce Robles

print("NÚMERO MAYOR DE TRES\n")

a = int(input("Ingrese el primer nro que sea entero: "))
b = int(input("Ingrese el segundo nro que sea entero: "))
c = int(input("Ingrese el tercer nro que sea entero: "))

if a > b and a > c:
    mayor = a
elif b > c and b > c:
    mayor = b
elif c > a and c > b:
    mayor = c
else:
    mayor = None



if mayor == None:
    print("\nNo se pude determinar el mayor, posiblemente sean los 3 iguales")
elif mayor % 2 == 0:
    print(mayor, "es el mayor y es par")
else:
    print(mayor, "es el mayor y es impar")