debe_pagar = None
continuar = True

while continuar:
    print("* Impuestonator 4000 *")
    if debe_pagar != None:
        print("")
        if debe_pagar:
            print("Ústed SI debe pagar el impuesto.")
        else:
            print("Ústed NO debe pagar el impuesto.")
    print("")
    print("1. Verificar por edad.")
    print("2. Salir.")
    print("")
    print("***********************")
    opcion = int(input("Ingrese una opción: "))

    while opcion < 1 or opcion > 2:
        opcion = int(input("Opción inválida. Ingrese de nuevo: "))
    
    if opcion == 1:
        print("\n"*20)

        edad = int(input("Ingrese su edad: "))

        print("")

        ingresos = int(input("Ingrese sus ingresos mensuales ($): "))

        if edad >= 18 and ingresos >= 100000:
            debe_pagar = True
        else:
            debe_pagar = False

        print("\n"*20)
    else:
        continuar = False

print("\n"*20)
print("¡Hasta luego!")