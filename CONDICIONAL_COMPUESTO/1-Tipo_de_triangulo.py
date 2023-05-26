#Introducir los lados de un triángulo y visualizar por pantalla si dicho
#triángulo es equilátero, isósceles o escaleno.
#Desarrollado por Emilce Robles

print("TIPO DE TRIANGULO\n")

lado_a = float(input("Ingrese la medida del 1er lado: "))
lado_b = float(input("Ingrese la medida del 2do lado: "))
lado_c = float(input("Ingrese la medida del 3er lado: "))

if lado_a == lado_b and lado_a == lado_c:
    print("\nEs un triándulo equilatero")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("\nEs un triándulo isosceles")
else:
    print("\nEs un triándulo escaleno")