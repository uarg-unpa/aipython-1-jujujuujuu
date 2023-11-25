# 11)
num = int(input("Ingrese un número: "))

for i in range(num+1):
    if i % 2 != 0:
        for j in range(i, 0, -1):
            if j % 2 != 0:
                print(j, end=" ")
        print()

print()

# 12)
num = int(input("Ingrese un número: "))
suma = 0
for i in range(num+1):
    if i == 0:
        continue
    elif i == num:
        print(i, end=" = ")
    else:
        print(i, end=" + ")
    suma += i

print(suma)
print()

# 13)
num = int(input("Ingrese un número: "))
suma = 0

for i in range(num+1):
    if i % 2 == 0:
        suma += i

print(suma)