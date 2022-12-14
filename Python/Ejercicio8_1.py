def crear ():
    nombreArchivo = input ("Ingrese el nombre del archivo: ")
    if (nombreArchivo == ""):
        print ("Debe ingresar un nombre de archivo")
    else:
        archivo = open (nombreArchivo, "w")
        archivo.close ()

def escribir ():
    nombreArchivo = input ("Ingrese el nombre del archivo: ")
    if not (nombreArchivo):
        print ("El archivo no existe")
    else:
        archivo = open (nombreArchivo, "a")
        archivo.write (input ("Ingrese el texto a agregar: "))
        archivo.close ()

def menu ():
    print("1. Crear archivo")
    print("2. Escribir archivo")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    while opcion != 3:
        match opcion:
            case 1:
                crear()
                return menu()
            case 2:
                escribir()
                return menu()
            case 3:
                print("Hasta luego")
                break
            case _:
                print("Opcion invalida")
                return menu()

if __name__ == '__main__':
    menu()