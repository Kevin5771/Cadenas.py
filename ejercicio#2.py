#Convertidor de cadenas en minusculas y mayusculas

nombre_completo = input("Por favor, Introduce tu Nombre Completo: ")

# El método .lower() convierte todos los caracteres en la cadena en minúsculas. 
nombre_minusculas = nombre_completo.lower()

# El método .upper convierte todos los caracteres en una cadena en Mayusculas
nombre_mayusculas = nombre_completo.upper()

#Este método convierte la primera letra de cada palabra en mayúscula y las demás letras en minúsculas. 
nombre_formateado = nombre_completo.title()

print("\nNombre completo en minúsculas:", nombre_minusculas)
print("Nombre completo en mayúsculas:", nombre_mayusculas)
print("Nombre completo formateado:", nombre_formateado)