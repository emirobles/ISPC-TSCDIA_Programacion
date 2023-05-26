#Realice un programa que lea dos números y diga cuál es el mayor.
#Desarrollado por Emilce Robles

print("EL MAYOR DE DOS NUMEROS\n")

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))

if a > b:
    print("\nEl mayor de los dos numeros es", a)
else:
    print("\nEl mayor de los dos numeros es", b)

if a ==b:
    print("\nNo se ha encontrado el mayor ya que ambos son iguales")