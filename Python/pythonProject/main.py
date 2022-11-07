class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def isAprobado(self):
        if self.nota >= 5:
            print("Alumno Aprobado")
        else:
            print("Alumno Reprobado")


Nombre = input("Ingrese el nombre del alumno: ")
Nota = int(input("Ingrese la nota del alumno: "))

a1 = Alumno(Nombre, Nota)
print("Nombre del Alumno: ", a1.nombre)
print("Nota ddel Alumno: ", a1.nota)
a1.isAprobado()
