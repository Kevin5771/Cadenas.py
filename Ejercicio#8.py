print("Ingrese el precio de un producto:")
precio = float(input(": "))

euros = int(precio)
centimos = int((precio - euros) * 100)

print("El precio es de " , euros ,  " euros y " , centimos , "centavos")
