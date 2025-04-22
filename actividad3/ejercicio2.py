cantidad_inicial = int(input("Ingresar la cantidad inicial en inventario"))
productos_recibidos = int(input("Ingresar la cantidad de productos recibidos"))
productos_vendidos = int(input("Ingresar la cantidad de productos vendidos"))
suma = productos_recibidos + cantidad_inicial
inventario_actual = suma - productos_vendidos
print(f"La cantidad inicial es de {cantidad_inicial}")
print(f"Los productos vendidos son:  {productos_vendidos} y los recibidos: {productos_recibidos} ")
print(f"La cantidad actual en inventario es: {inventario_actual}")