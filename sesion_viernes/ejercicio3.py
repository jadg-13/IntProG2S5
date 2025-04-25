print("Presiona Cero para salir")
dia = int(input("Ingrese el dia de la semana de forma númerica(1-7): "))

while dia != 0:
    if dia==1:
        print("Lunes")
    elif dia ==2:
        print("Martes")
    elif dia==3:
        print("Miércoles") 
    elif dia==4:
        print("Jueves") 
    elif dia==5:
        print("Viernes")
    elif dia==6:
        print("Sábado")
    elif dia==7:
        print("Domingo")
    else:
        print("Error. El número digitado no es válido")
        
    print("Presiona Cero para salir")
    dia = int(input("Ingrese el dia de la semana de forma númerica(1-7): "))