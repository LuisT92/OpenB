from functools import reduce


def solicitaNumeros():
     numeros = []
     print("1: Ingreasr numero")
     print("2: Salir")
     opcion = int(input("Ingrese opcion: "))
     while opcion != 2:
        numero = int(input("Ingrese numero: "))
        numeros.append(numero)
        opcion = int(input("Ingrese opcion: "))
     return numeros

if __name__ == "__main__":
    numeros = solicitaNumeros()
    lista = list(filter(lambda par: par % 2 != 0, numeros))
    print(f'Los numeros impares de los ingresados son: {lista}')
    suma= reduce(lambda x, y: x + y, lista)
    print(f'La suma de los numeros impares ingresados es: {suma}')
