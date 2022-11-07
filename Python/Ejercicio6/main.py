class Vehiculo():
  def __init__(self):
    self._ruedas = 4
    self._color = "Rojo"
    self._puertas = 4
class coche(Vehiculo):
    def __init__(self):
        super().__init__()
        self._velocidad = 0
        self._cilindrada = 1.6

automovil = coche()
print("Descripcion del coche: ")
print("Color:", automovil._color)
print("Numero de ruedas:", automovil._ruedas)
print("Numero de puertas:", automovil._puertas)
print("Velocidad:", automovil._velocidad)
print("Cilindrada:", automovil._cilindrada)