precio = float(input("Ingrese el precio de un producto: "))

euros = int(precio)
centimos = int((precio - euros) * 100)

print("El precio es de " , euros ,  " euros y " , centimos , "centavos")
