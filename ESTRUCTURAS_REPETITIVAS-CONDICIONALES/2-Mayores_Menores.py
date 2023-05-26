#Leer 10 números y obtener la cantidad de mayores y la cantidad de
#menores a 100, cuál es el número máximo y cuál es el número mínimo.
#Desarrollado por Emilce Robles

print("MAYORES Y MENORES\n")

def mayores_menores(): #Funcion
    numeros = [] #Lista vacia
    mayores_a_100 = 0 #Iniciación de variable numerica
    menores_a_100 = 0 #Iniciación de variable numerica

    for i in range(10): #Ciclo para iterar numeros que se vayan ingresando
        numero = float(input(f">>Ingrese el {i + 1}° número : ")) #Admite el ingreso de numeros flotantes
        numeros.append(numero) #Se agrega numero a la lista "numeros"
        if numero > 100: # condicional para evaluar si el numero es mayor a 100
            mayores_a_100 += 1 # Sumador para el contador de mayores
        elif numero < 100: # condicional para evaluar si el numero es menor a 100
            menores_a_100 += 1 # Sumador para el contador de menores

    numero_maximo = max(numeros) #Se calcula cuando de todos los numeros agregados a la lista es el mayor
    numero_minimo = min(numeros)  #Se calcula cuando de todos los numeros agregados a la lista es el menor

    print("\n-Cantidad de números mayores a 100:", mayores_a_100) #Salida de resultados para indicar total de mayores a 100
    print("\n-Cantidad de números menores a 100:", menores_a_100) #Salida de resultados para indicar total de menores a 100
    print("\n-Número máximo:", numero_maximo) #Salida de resultados para indicar nro maximo
    print("\n-Número mínimo:", numero_minimo) #Salida de resultados para indicar nro menor

mayores_menores() #invoca a la funcion