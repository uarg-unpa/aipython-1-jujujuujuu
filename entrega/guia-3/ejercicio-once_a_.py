# 11)
num = int(input("Ingrese un número: "))

for i in range(num+1):
    if i % 2 != 0:
        for j in range(i, 0, -1):
            if j % 2 != 0:
                print(j, end=" ")
        print()