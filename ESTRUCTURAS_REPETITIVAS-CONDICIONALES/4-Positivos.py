#Leer 10 números y mostrar solamente los números positivos, y su
#sumatoria.
#Desarrollado por Emilce Robles

print("NUMEROS POSITIVOS\n")

def positivos(): #Funcion
    numeros_positivos = [] #Lista vacia
    sumatoria = 0 #Iniciación de variable numerica

    for i in range(10): #Ciclo para iterar numeros que se vayan ingresando
        numero = float(input(f">>Ingrese el {i + 1}° número: ")) #Admite el ingreso de numeros flotantes
        
        if numero > 0: # condicional para evaluar si se trata de nros positivos
            numeros_positivos.append(numero) #Se agrega el nro positivo a la lista
            sumatoria += numero #Contador con la sumatoria de los valores de nros positivos

    print("\n- Números positivos ingresados:", numeros_positivos) #Salida de resultados con los nros positivos
    print("\n- Sumatoria de los números positivos:", sumatoria) #Salida de resultados con los nros positivos

positivos() #invoca a la funcion