# 14)
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

mayor = num1 > num2 and num1 or num2
menor = mayor == num1 and num2 or num1

for i in range(menor+1, mayor):
    if i % 2 == 0:
        print(i, end=", ")
print()
print()

# 15)
num = int(input("Ingrese un número: "))

for i in range(num+1):
    if i < 2:
        continue

    if num % i == 0:
        print(i != num and "No Primo" or "Primo")
        break