#Realice un programa que lea 4 números y diga cuántos son pares y
#cuantos impares y devuelva la sumatoria de los pares.
#Desarrollado por Emilce Robles

print("PARES E IMPARES\n")

def pares_impares(): #Funcion
    numeros = [] #Lista vacia
    pares = 0 #Iniciación de variable numerica
    sumatoria_pares = 0 #Iniciación de variable numerica

    for i in range(4): #Ciclo para iterar numeros que se vayan ingresando
        numero = int(input(f">>Ingrese el número {i + 1}: ")) #Admite el ingreso de numeros enteros
        numeros.append(numero) #Se agrega numero a la lista "numeros"
        
        if numero % 2 == 0: # condicional para evaluar si el numero es par
            pares += 1 # Contador de nros pares
            sumatoria_pares += numero # Sumatoria de los valores de los numeros pares
    
    impares = 4 - pares #Calculo de cantidad de nros impares

    print(f"\n- Cantidad de números pares: {pares}") #Salida de resultados para indicar nros pares totales
    print(f"\n- Cantidad de números impares: {impares}") #Salida de resultados para indicar nros impares totales
    print(f"\n- Suma de los números pares: {sumatoria_pares}") #Salida de resultados para indicar suma de los valores de nros pares


pares_impares() #invoca a la funcion
