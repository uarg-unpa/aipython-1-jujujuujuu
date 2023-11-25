def calcularIMC(p, a):
    return p*(a**2)

imc = None
continuar = True

while continuar:
    print("*  Calculador de Indice de Masa Corporal (IMC) *")
    if imc:
        print("")
        print("Su IMC es de:", imc)
    print("")
    print("1. Calcular IMC.")
    print("2. Salir.")
    print("")
    print("****************© E & S Studios.****************")
    opcion = int(input("Ingrese opción: "))
    
    #validacion de opcion
    while opcion < 1 or opcion > 2:
        opcion = int(input("Eleccion erronea, reingrese por favor: "))

    if opcion == 1:
        print("\n"*20)

        peso = int(input("Ingrese su peso (kg): "))

        print("")

        altura = float(input("Ingrese su altura (metros): "))

        print("\n"*20)
        imc = calcularIMC(peso, altura)
    else:
        continuar = False

print("")
print("¡Hasta pronto!")
print("© E & S Studios.")