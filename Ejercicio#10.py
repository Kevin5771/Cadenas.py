# Separar los productos por comas y almacenarlos en una lista
print("Introduce los productos de la cesta de compra separados por comas: ")
lista_productos = input(": ").split(',')

if lista_productos:
    print("Productos en la cesta de compra:")
    for producto in lista_productos:
        # El metodo stip elimina los espacios de una cadena al incio y al final.
        producto_limpio = producto.strip()  
        print(producto_limpio)
