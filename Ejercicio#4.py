
print ("Por favor, introduce tú número de teléfono en el formato +34-XXXXXX-XX: ")

num_telefono = input(": ")

# Separa un arreglo o lista con el method "split"
parts = num_telefono.split("-")
num_prefijo = parts[1]

# Imprimir el número sin el prefijo y la extensión
print( " Tú Número de teléfono sin prefijo y extensión: ", num_prefijo)