contraseña = input("Asigne una contraseña: ")

def verificar_contraseña():
    print("")

    if input("Introduzca la contraseña: ").lower() == contraseña.lower():
        print("Las contraseña es correcta.")
    else:
        print("Las contraseñas NO es correcta.")
        verificar_contraseña()

verificar_contraseña()