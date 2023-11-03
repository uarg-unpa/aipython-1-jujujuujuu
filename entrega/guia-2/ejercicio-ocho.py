precio = None
continuar = True

while continuar:
    print("* © Juegos Gaming Inc. *")
    if precio:
        print("")
        print("¡Gracias por realizar su compra!")
        print(f"Se le ha cobrado: ${precio}")
    print("")
    print("1. Comprar una entrada.")
    print("2. Salir.")
    print("")
    print("************************")
    opcion = int(input("Ingrese una opción: "))

    while opcion < 1 or opcion > 2:
        opcion = int(input("Opción inválida. Ingrese de nuevo: "))
    
    if opcion == 1:
        print("\n"*20)

        edad = int(input("Ingrese la edad del cliente: "))

        if edad < 4:
            precio = 0
        elif edad > 3 and edad < 19:
            precio = 5
        elif edad > 18:
            precio = 10

        print("\n"*20)
    else:
        continuar = False

print("\n"*20)
print("¡Hasta luego!")
print("© Juegos Gaming Inc.")