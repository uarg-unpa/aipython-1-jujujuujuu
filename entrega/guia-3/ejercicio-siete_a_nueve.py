# 7)
nombre = input("Ingrese su nombre: ")
repeticiones = int(input("Ingrese un número: "))

for i in range(repeticiones):
    print(nombre)

# 8)
num = int(input("Ingrese un número mayor a 3: "))

while num <= 3:
    num = int(input("ERROR, el número no es mayor a 3: "))

for i in range(num):
    if i % 2 != 0:
        print(i)

print()

# 9)
for i in range(10):
    print(f"{i} x {i} = {i*i}")