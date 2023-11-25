sueldo = None
continuar = True
while continuar:
    print("*      Calculador de Sueldo      *")
    if sueldo:
        print("")
        print(f"Su sueldo es de: ${sueldo}")
    print("")
    print("1. Calcular sueldo.")
    print("2. Salir.")
    print("")
    print("*********© E & S Studios.**********")
    opcion = int(input("Ingrese opción: "))
    
    #validacion de opcion
    while opcion < 1 or opcion > 2:
        opcion = int(input("Eleccion erronea, reingrese por favor: "))

    if opcion == 1:
        print("\n"*20)

        costo_hora = float(input("Ingrese el costo por hora: "))

        print("")

        horas_trabajadas = float(input("Ingrese las horas trabajadas: "))

        sueldo = costo_hora * horas_trabajadas
        print("\n"*20)
    else:
        continuar = False

print("")
print("¡Hasta pronto!")
print("© E & S Studios.")