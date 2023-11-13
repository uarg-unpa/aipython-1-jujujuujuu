def obtener_tabla(x=10):
    tabla = []

    for i in range(10):
        mult = i+1
        resultado = x*mult

        tabla.append(resultado)
        print(f"{x} x {mult} = {resultado}")
    
    return tabla

obtener_tabla()