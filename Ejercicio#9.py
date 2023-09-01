# Solicitamos al usuario que introduzca su fecha de nacimiento
fecha_nacimiento = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")

# Usamos el método split para dividir la entrada en tres partes usando '/' como separador,
day, month, year = map(int, fecha_nacimiento.split('/'))

print(f"Día: {day}")
print(f"Mes: {month}")
print(f"Año: {year}")
