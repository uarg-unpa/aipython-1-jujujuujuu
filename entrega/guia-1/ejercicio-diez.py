temp_farenheit = None
continuar = True

while continuar:
    print("*       Conversor de Celsius a Farenheit       *")
    if temp_farenheit:
        print("")
        print(f"Su temperatura es de: {temp_farenheit}°F")
    print("")
    print("1. Convertir.")
    print("2. Salir.")
    print("")
    print("****************© E & S Studios.****************")
    opcion = int(input("Ingrese opción: "))
    
    #validacion de opcion
    while opcion < 1 or opcion > 2:
        opcion = int(input("Eleccion erronea, reingrese por favor: "))

    if opcion == 1:
        print("\n"*20)

        temp_celsius = float(input("Ingrese la temperatura: "))

        temp_farenheit = (temp_celsius * 9/5) + 32
        print("\n"*20)
    else:
        continuar = False

print("")
print("¡Hasta pronto!")
print("© E & S Studios.")