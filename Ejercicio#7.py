
print("Ingrese un correo electronico: ")
correo = input(": ")
option_1 = "gmail"
replace_1 = "ceu"
option_2 = ".com"
replace_2 = ".es"

nuevocorreo = correo.replace(option_1, replace_1)
nuevo_correo2 = nuevocorreo.replace(option_2, replace_2)

print(nuevo_correo2)
