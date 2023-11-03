edad1 = int(input("Ingrese su edad: "))
edad2 = int(input("Ingrese otra edad: "))

if edad1 == edad2:
    print("Tenemos la misma edad, y aún asi sigo siendo más inmaduro ☺")
elif edad1 > edad2:
    print("Eres mayor.")
    if edad1-edad2 > 1:
        print("años")
    else:
        print("año")
else:
    print("Soy mayor.")
    if edad2-edad1 > 1:
        print("años")
    else:
        print("año")