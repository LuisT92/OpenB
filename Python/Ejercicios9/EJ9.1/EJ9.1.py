def ingresaPaises():
    paises = set()
    print("1: Ingreasr pais")
    print("2: Salir")
    opcion = int(input("Ingrese opcion: "))
    while opcion != 2:
        pais = input("Ingrese pais: ")
        paises.add(pais)
        opcion = int(input("Ingrese opcion: "))
    return paises

if __name__ == "__main__":
    paises = ingresaPaises()
    print(sorted(paises))
