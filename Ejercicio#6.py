print ("Escribe una Frase: ")
frase = input (": ")

print ("Esscribe una Vocal: ")
vocal_1= input(": ")

# Reemplaza la vocal introducida por su versión en mayúscula en la frase.
frase_modificada = frase.replace(vocal_1, vocal_1.upper())

# Imprime la frase modificada que ahora contiene la vocal en mayúscula.
print("Frase Modificada:", frase_modificada)
