def esBiciesto(anio):
    if anio%4==0 and anio%100!=0 or anio%400==0:
        return True
    else:
        return False

anio=input("Introduce el año: ")
biciesto= esBiciesto(int(anio))
if biciesto:
    print("El año es biciesto")
else:
    print("El año no es biciesto")


