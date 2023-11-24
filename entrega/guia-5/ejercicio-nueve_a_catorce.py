# 9)
def mult_list(list):
    x = 1

    for num in list:
        x *= num

    return x

print(mult_list([2, 4, 1, 5]))
print()

# 10)
def es_palindromo(string):
    return string == string[::-1]

print(es_palindromo("aibofobia"))

# 11)
def farenheit_a_celsius(temp):
    return (temp - 32) * (5/9)

print(farenheit_a_celsius(50))
print()

# 12)
def cont_vocales(string: str):
    vocales = ["a", "e", "i", "o", "u"]
    cont = 0

    for letra in string:
        if letra.lower() in vocales:
            cont += 1
    
    return cont

print(cont_vocales("Hola, ¿Como estan muchachos?"))
print()

# 13)
def intercalar_listas(lista1, lista2):
    intercalada = []
    menor = len(lista1) < len(lista2) and lista1 or lista2
    mayor = menor == lista1 and lista2 or lista1

    for i in range(len(menor)):
        intercalada.append(lista1[i])
        intercalada.append(lista2[i])
    
    intercalada.extend(mayor[len(menor)::])

    return intercalada

print(intercalar_listas([1, 2, 3, 4, 5, 6], ["a", "b", "c"]))
print()

# 14)
def promedio(lista):
    promedio = 0

    for i in lista:
        promedio += i

    return promedio/len(lista)

print(promedio([4, 2, 8, 2, 20]))