a = float(input("Introduzca un número A: "))
b = float(input("Introduzca un número B: "))

print("")

if a > b:
    print("A es mayor a B")
elif a < b:
    print("B es mayor a A")
else:
    print("A es igual a B")

print("")

if int(input("Ingrese un número entero: ")) % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")