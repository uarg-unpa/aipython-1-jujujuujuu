retribucion = None
continuar = True

while continuar:
    print("*       Calculador de inversiones anuales       *")
    if retribucion:
        print("")
        print(f"Su retribución es de: ${retribucion}")
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

        inversion = float(input("Ingrese la inversion ($): "))

        print("")

        interes = int(input("Ingrese el interés anual (%): "))

        #verificar que el interes no sea erroneo
        while interes < 0 or interes > 100:
            interes = int(input("Error, número mayor a cien o menor a 0"))

        print("")

        años = int(input("Ingrese el número de años: "))

        retribucion = (inversion*(interes/100))*años
        print("\n"*20)
    else:
        continuar = False

print("")
print("¡Hasta pronto!")
print("© E & S Studios.")