import pickle


class vehiculo:
    def __init__(self, marca, modelo, color, precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio

    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getColor(self):
        return self.color
    def getPrecio(self):
        return self.precio


def guardar_vehiculo(vehiculo):
    vehiculo_guarda = open("vehiculos.bin", "wb")
    pickle.dump(vehiculo, vehiculo_guarda)
    vehiculo_guarda.close()
def leer_vehiculo():
    vehiculo_leer = open("vehiculos.bin", "rb")
    auto = pickle.load(vehiculo_leer)
    print("Marca:", auto.getMarca(), "Modelo:", auto.getModelo(), "Color:", auto.getColor(), "Precio: $", auto.getPrecio())
    vehiculo_leer.close()

def menu():
    print("1. Guardar vehiculo")
    print("2. Leer vehiculo")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    while opcion != 3:
        match opcion:
            case 1:
                auto_nuevo = vehiculo(input("Ingrese la marca:"), input("Ingrese el modelo:"), input("Ingrese el color:"), input("Ingrese el precio:"))
                guardar_vehiculo(auto_nuevo)
                return menu()
            case 2:
                leer_vehiculo()
                return menu()
            case 3:
                break
            case _:
                print("Opcion invalida")
                return menu()
    print("Hasta luego")
if __name__ == '__main__':
    menu()