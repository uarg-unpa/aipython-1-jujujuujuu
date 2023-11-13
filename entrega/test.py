def obtener_tabla(x=10):
    tabla = []

    for i in range(1, 11):
        resultado = x*i
        tabla.append(resultado)
        print(f"{x} x {i} = {resultado}")

    return tabla

#print(obtener_tabla(15))

def mayor_de_tres(num1, num2, num3):
    x = num1 > num2 and num1 or num2
    return x > num3 and x or num3

#print(mayor_de_tres(1, 2, 3))

def obtener_mayor(nums):
    mayor = nums[0]

    for i in nums:
        if i > mayor:
            mayor = i
    
    return mayor

print(obtener_mayor([30, -22, 100, 3]))

def suma_lista(lista):
    suma = 0

    for i in lista:
        suma += i

    return suma

print(suma_lista([1, 5, 2, 3]))