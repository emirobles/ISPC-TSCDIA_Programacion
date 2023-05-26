#Ingresar las edades y el sexo de 15 personas y determinar cuántas son
#mujeres, cuántos varones, cuántos mayores de edad y cuántos
#menores de edad.
#Desarrollado por Emilce Robles

print("EDADES Y GENERO")

def genero_x_edades(): #Funcion
    mujeres = 0 #Iniciación de variable numerica
    varones = 0 #Iniciación de variable numerica
    mayores_edad = 0 #Iniciación de variable numerica
    menores_edad = 0 #Iniciación de variable numerica

    for i in range(15): #Ciclo para iterar datos que se vayan ingresando
        edad = int(input("\nIngrese la edad de la persona {}: ".format(i+1))) #Admite el ingreso de numeros enteros
        sexo = input("Ingrese el sexo de la persona {} (M/F): ".format(i+1)) #Admite el ingreso de cadena de caracteres (string)
        
        if sexo == "F" or sexo == "f": # condicional para evaluar si el caracter ingresado es F que representa al Genereo femenino
            mujeres += 1 # Contador de genero femenino
        elif sexo == "M" or sexo == "m": # condicional para evaluar si el caracter ingresado es M que representa al Genereo masculino
            varones += 1 # Contador de genero masculino
        
        if edad >= 18: # condicional para evaluar si la edad es mayor o igual a 18
            mayores_edad += 1 # Contador de mayores
        else: # condicional para el resto de las edades que son menores
            menores_edad += 1 # Contador de menores

    print("\n- Cantidad de mujeres:", mujeres) #Salida de resultados totales de mujeres
    print("\n- Cantidad de varones:", varones) #Salida de resultados totales de varones
    print("\n- Cantidad de personas mayores de edad:", mayores_edad) #Salida de resultados totales de mayores de edad
    print("\n- Cantidad de personas menores de edad:", menores_edad) #Salida de resultados totales de menoress de edad

genero_x_edades() #invoca a la funcion