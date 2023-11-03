def verificar_edad():
    edad = int(input("Ingrese su edad: "))

    if edad >= 18:
        print("Tiene suficiente edad para conducir.")
    else:
        print("Le faltan", 18-edad, "años para poder conducir!")

    print("")
    verificar_edad()

verificar_edad()