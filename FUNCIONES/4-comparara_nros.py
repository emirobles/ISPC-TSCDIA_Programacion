def comparar_2_numeros(num1, num2):
    if num1 == num2:
        print(f"{True}. Ambos numeros son iguales")
    else:
        print(f"{False}. Los numeros ingresados son diferentes2")


# Ingreso de los números a comparar
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))


# Comparación de los números ingresados y llamada de la funcion
comparar_2_numeros(numero1, numero2)