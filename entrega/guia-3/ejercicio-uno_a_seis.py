# 1)
cont = 0

while cont < 101: # 101 para que se muestre del 0 al 100 en la terminal
    print(cont)
    cont += 1

print("\n"*5)

# 2)
for i in range(101):
    print(i)

print("\n"*5)

# 3)
cont2 = 10

while cont2 > 0:
    print(cont2)
    cont2 -=1

print()

for i in range(10, 0):
    print(i)

# 4)
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

print()

mayor = num1 > num2 and num1 or num2
menor = mayor == num1 and num2 or num1

for i in range(menor+1, mayor):
    print(i)

print()

# 5)
for i in range(8):
    print("#"*i)

print()

# 6)
for _ in range(8):
    for _ in range(8):
        print("#", end="")
    print()