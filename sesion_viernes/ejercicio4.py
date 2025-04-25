#Funcion
"""
     Crea un programa que reciba tres números y determine si pueden formar un triángulo. Un triángulo es válido si la suma de las longitudes de dos lados es siempre mayor que la longitud del tercer lado.
"""

def es_triangulo(lado1, lado2, lado3):
    suma = lado1 + lado2
    if(suma > lado3):
        return "Es un triangulo"
    else:
        return "No es un triangulo"

def main():
    print("Ingresa los siguientes valores ")
    print("="*30)
    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    lado3 = float(input("Lado 3: "))
    print(es_triangulo(lado1, lado2, lado3))

main()