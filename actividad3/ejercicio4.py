distancia_km = float(input("Ingrese la cantidad recorrida en kilometros:"))
litros_consum = float(input("Ingrese la cantidad de litros consumidos:"))

rendimiento = distancia_km/litros_consum
gasto_combustible = litros_consum * 39.58

print(f"La distancia recorrida en kilometros es de: {distancia_km}")
print(f"Los litros de gasolina consumidos en litros es de :{litros_consum}")
print(f"El precio por litros es de: 39.58")
print(f"El rendimiento es de: {rendimiento}")
print(f"El gasto total en combustible es de: {gasto_combustible:.2f}")
