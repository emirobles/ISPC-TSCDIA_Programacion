#Leer 15 números negativos y convertirlos a positivos e imprimir dichos
#números.
#Desarrollado por Emilce Robles

print("NUMEROS NEGATIVOS A POSITIVOS\n")

def negativo_a_positivo(): #Funcion
    numeros_positivos = [] #Lista vacia

    for i in range(15): #Ciclo para iterar numeros ingresados
        numero = float(input("Ingrese un número negativo: "))
        
        while numero >= 0: #Verifica que los numeros ingresados sean negativos para poder avanzar
            print("Debe ingresar un número negativo. Inténtelo nuevamente.") #Salida para dar aviso y reiterar acción
            numero = float(input("Ingrese un número negativo: ")) #Permite ingreso de numeros flotantes
        
        numero = abs(numero) # Convierte el número a positivo utilizando la función abs()
        numeros_positivos.append(numero) #Agrega el numero a la lista

    print("\n- Números convertidos a positivos:", numeros_positivos) #Salida para mostrar los numeros que han pasado a ser positivos

negativo_a_positivo()

#Desarrollado por Emilce Robles