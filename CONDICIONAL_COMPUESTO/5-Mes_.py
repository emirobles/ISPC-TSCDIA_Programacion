#Realice un programa que pida un número del 1 al 12 y diga el nombre
#del mes correspondiente.
#Desarrollado por Emilce Robles

print("MES DEL AÑO")

mes = int(input("Ingrese un número entero del 1 al 12: "))

if mes == 1:
    print("\nHa elegido el mes de Enero")
elif mes == 2:
    print("\nHa elegido el mes de Febrero")
elif mes == 3:
    print("\nHa elegido el mes de Marzo")
elif mes == 4:
    print("\nHa elegido el mes de Abril")
elif mes == 5:
    print("\nHa elegido el mes de Mayo")
elif mes == 6:
    print("\nHa elegido el mes de Junio")
elif mes == 7:
    print("\nHa elegido el mes de Julio")
elif mes == 8:
    print("\nHa elegido el mes de Agosto")
elif mes == 9:
    print("\nHa elegido el mes de Septiembre")
elif mes == 10:
    print("\nHa elegido el mes de Octubre")
elif mes == 11:
    print("\nHa elegido el mes de Noviembre")
elif mes == 12:
    print("\nHa elegido el mes de Diciembre")
else:
    print("\nEl valor ingresado es incorrecto")