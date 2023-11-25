# 1) y 2)
def multiplicar(x = 1, y = 1):
    return x * y

print(multiplicar(5, 5))
print()

# 3)
def algo_creativo(nombre: str):
    return "La aibofobia es el miedo irracional a los palíndromos, "+nombre[::-1]+nombre[1:]

print(algo_creativo("Pancracio"))
print()

# 4)
def obtener_tabla(x=10):
    tabla = []

    for i in range(1, 11):
        resultado = x*i
        tabla.append(resultado)
        print(f"{x} x {i} = {resultado}")

    return tabla

obtener_tabla(2)
print()

# 5)
def es_par(x = 2):
    return x % 2 == 0

print(es_par(63))
print()

# 6)
def factorial(x):
    y = 1

    for i in range(1, x+1):
        y *= i

    return y

print(factorial(7))
print()

# 7)
def mayor_de_tres(num1, num2, num3):
    x = num1 > num2 and num1 or num2
    return x > num3 and x or num3

print(mayor_de_tres(14, 2, 7))
print()

# 8)
def reverse_str(string):
    return string[::-1]

print(reverse_str("Hola"))