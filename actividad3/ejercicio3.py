capital_inicial = float(input("Ingrese el capital inicial: "))
tasa_interes = float(input("Ingrese la tasa de interés en porcentaje: "))
tiempo = float(input("Ingrese la cantidad de años: "))

tasa_interes_dec = tasa_interes / 100
monto_final = ((1 + tasa_interes_dec)**tiempo)*capital_inicial
interes_ganado = monto_final - capital_inicial

print(f"Capital inicial: {capital_inicial:.2f}")
print(f"Tasa: {tasa_interes:.2f}")
print(f"Años: {tiempo:.2f}")
print(f"Monto final: {monto_final:.2f}")
print(f"Interés ganado: {interes_ganado:.2f}")
