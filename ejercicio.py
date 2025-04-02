# Número secreto definido
numero_secreto = 5
# importar la librería random para generar un número secreto aleatorio
print("¡Bienvenido al juego de adivinar el número!")
print("Escribe 'salir' en cualquier momento para terminar el juego.")

while True:
    # Pedir al usuario que adivine el número
    entrada = input("Adivina el número secreto: ")

    # Verificar si el usuario quiere salir
    if entrada.lower() == "salir":
        print("¡Gracias por jugar! Hasta luego.")
        break

    # Intentar convertir la entrada a un número
    try:
        numero_adivinado = int(entrada)
    except ValueError:
        print("Por favor, ingresa un número válido o escribe 'salir' para terminar.")
        continue

    # Comparar el número ingresado con el número secreto
    if numero_adivinado == numero_secreto:
        print("¡Felicidades! Adivinaste el número secreto.")
        break
    #aca hacemos un codigo que nos hace decir que si el unmero es mayori o menos , e lo comenta al darte una respuesta para que sigas con el problema
    elif numero_adivinado < numero_secreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    else:
        print("El número secreto es menor. Intenta de nuevo.")