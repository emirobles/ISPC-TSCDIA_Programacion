#Confeccione un programa que pida un número del 1 al 7 y diga el día de
#la semana correspondiente.
#Desarrollado por Emilce Robles

print("DIA DE LA SEMANA\n")

dia = int(input("Ingrese un número entero del 1 al 7: "))

if dia == 1:
    print("\nHa elegido el día Lunes")
elif dia == 2:
    print("\nHa elegido el día Martes")
elif dia == 3:
    print("\nHa elegido el día Miercoles")
elif dia == 4:
    print("\nHa elegido el día Jueves")
elif dia == 5:
    print("\nHa elegido el día Viernes")
elif dia == 6:
    print("\nHa elegido el día Sábado")
elif dia == 7:
    print("\nHa elegido el día Domingo")
else:
    print("\nEl valor ingresado es incorrecto")