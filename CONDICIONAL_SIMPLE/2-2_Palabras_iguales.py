#Hacer un programa que permita decidir si dos palabras son iguales o
#diferentes. Mostrar mensaje por pantalla.
#Desarrollado por Emilce Robles

print("COMPARACIÓN DE 2 PALABRAS\n")

a=input("Ingrese la primer palabra: ")
b=input("Ingrese la segunda palabra: ")

if a.lower() == b.lower():
    print("\n->Ambas palabras son iguales")
else:
    print("\n->Las palabras ingresadas son diferentes")
print("\nGracias por su consulta")