import math

area = None
perimetro = None
continuar = True

while continuar:
    print("*        Calculador de Área y Perímetro        *")
    if area and perimetro:
        print("")
        print("Su perímetro es de:", perimetro)
        print("Su área es de: ", area)
    print("")
    print("1. Calcular para rectángulo.")
    print("2. Calcular para circunferencia.")
    print("3. Salir.")
    print("")
    print("************************************************")
    opcion = int(input("Ingrese opción: "))
    
    #validacion de opcion
    while opcion < 1 or opcion > 2:
        opcion = int(input("Eleccion erronea, reingrese por favor: "))

    if opcion == 1:
        print("\n"*20)

        base = int(input("Ingrese base: "))

        print("")

        altura = int(input("Ingrese altura: "))

        perimetro = 2*base + 2*altura
        area = base*altura
        print("\n"*20)
    elif opcion == 2:
        print("\n"*20)

        radio = int(input("Ingrese el radio: "))

        perimetro = 2*math.pi*radio
        area = math.pi*(radio**2)
        print("\n"*20)
    else:
        continuar = False

print("")
print("¡Hasta pronto!")
print("© E & S Studios.")