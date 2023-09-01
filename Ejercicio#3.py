nombre = input("Por favor, introduce tu nombre: ")

# El método .upper convierte todos los caracteres en una cadena en Mayusculas
nombre_mayusculas = nombre.upper()
# Este método nos da las dimensciones de una cadena.
longitud_nombre = len(nombre)

# Impresión final
print(f"{nombre_mayusculas} tiene {longitud_nombre} letras.")