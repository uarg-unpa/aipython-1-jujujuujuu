dia = int(input("Ingrese un número (1-7): "))

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("No es un número válido.")

nota = int(input("Ingrese una nota (0-100): "))

if nota >= 0 and nota < 50:
    print("F")
elif nota > 49 and nota < 60:
    print("D")
elif nota > 59 and nota < 70:
    print("C")
elif nota > 69 and nota < 90:
    print("B")
elif nota > 89 and nota <= 100:
    print("A")
else:
    print("ERROR: número inválido.")