def intercambiar_mensajes():
    aula1 = input("Ingrese el número de Aula 1: ")
    mensaje_adicional1 = input("Ingrese el mensaje adicional 1: ")
    aula2 = input("Ingrese el número de Aula 2: ")
    mensaje_adicional2 = input("Ingrese el mensaje adicional 2: ")
    aula3 = input("Ingrese el número de Aula 3: ")
    mensaje_adicional3 = input("Ingrese el mensaje adicional 3: ")

    print(f"Hola Aula {aula1}, ¿Qué tal?")
    print(mensaje_adicional1)
    print(f"Hola Aula {aula2}, ¿Qué tal?")
    print(mensaje_adicional2)
    print(f"Hola Aula {aula3}, ¿Qué tal?")
    print(mensaje_adicional3)

# Llamada de la función
intercambiar_mensajes()