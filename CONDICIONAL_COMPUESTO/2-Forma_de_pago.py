#Realice un programa que le permita al usuario simular el pago
#ingresando el importe y la forma de pago:
#• Contado (1): se aplica un descuento del 10% al importe
#• Tarjeta (2): se aplica un interés de 10%
#• Débito (3): se aplica un descuento del 5%
#Mostrar el importe, el descuento o interés y el importe total.
#Desarrollado por Emilce Robles

print("FORMA DE PAGO\n")

importe = float(input("Ingrese el importe que desea abonar: "))

print("Formas de pago disponibles:\n")
print("1) Contado\n")
print("2) Tarjeta de Crédito\n")
print("3) Debito\n")

opcion = int(input("Ingrese el Nro de la forma elegida: "))

if opcion == 1:
    descuento = (importe * 10) / 100
    imp_final = round((importe - descuento), 2)
    print("\nEl valor a abonar es de: $", imp_final)
elif opcion == 2:
    interes = (importe * 10) / 100
    imp_final = round((importe + interes), 2)
    print("\nEl valor a abonar es de: $", imp_final)
elif opcion == 3:
    descuento_deb = (importe * 5) / 100
    imp_final = round((importe - descuento_deb), 2)
    print("\nEl valor a abonar es de: $", imp_final)
else:
    print("\nLa opcion ingresada no es valida")