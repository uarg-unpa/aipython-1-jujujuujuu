# 1) a 3)
lista_vacia = []
lista1 = [1,3,4,5,6,7,8]
print(len(lista1))

# 4)
frutas_favoritas = ["Manzana", "Durazno", "Banana", "Ananá"]
print(len(frutas_favoritas))
frutas_favoritas.pop(0)
print(frutas_favoritas)
frutas_favoritas.append("Manzana")
print(frutas_favoritas)

# 5)
longitud = len(lista1)-1
print(lista1[0], lista1[int(longitud/2)], lista1[longitud])

# 6)
datos_personales = []
datos_personales.append("Ethan Butterfield")
datos_personales.append(15)
datos_personales.append(1.62)
datos_personales.append("Rio Gallegos, Santa Cruz, Argentina")
datos_personales.append("Soltero")

# 7)
companias_favoritas = ["Roblox", "DICE", "Felfort", "Microsoft", "SpaceX", "Fazbear Ent."]

# 8)
for dato in datos_personales:
    print(dato)

print()

# 9)
for i in range(len(companias_favoritas)):
    print(i, companias_favoritas[i])

print()

# 10)
companias_favoritas[5] = "NVidia"
print(companias_favoritas)