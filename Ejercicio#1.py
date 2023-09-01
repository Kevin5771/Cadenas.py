def imprimir_nombre(usuario, repeticiones):
    if repeticiones <= 0:
        return
    print(usuario)
    imprimir_nombre(usuario, repeticiones - 1)

nombre_usuario = input("Ingresa tu nombre: ")
numero_repeticiones = int(input("Ingresa un número entero: "))

imprimir_nombre(nombre_usuario, numero_repeticiones)