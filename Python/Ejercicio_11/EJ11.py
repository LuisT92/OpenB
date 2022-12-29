import sqlite3

# Conectamos con la base de datos
# siempre se abre y cierra la conexión como en java o en la mayoría de lenguajes de programación
# para evitar problemas de concurrencia y demás problemas de seguridad y rendimiento

#conn = sqlite3.connect('alumnosdb.db')
#cursor = conn.cursor()
# para iniciar a hacer las consultas a la base de datos se usa el método execute
# para hacer consultas de selección se usa el método fetchall
# para hacer consultas de inserción, actualización y borrado se usa el método commit para guardar despues de ejecutar la query
# y para poder visualizar los datos se debe asignar a una variable el resultado de la consulta, comunmente
# con isolation_level=None se evita que se haga un commit automatico al final de cada consulta y lo que contiene el cursor se envia automatico
# se usa el nombre de la variable row
#row = cursor.execute("SELECT * FROM alumnos")
# aunque no es totalmente necesario como buena practica esta biencerrar el cursor tambien
#cursor.close()
# conn.close()

# Ejercicio 11

def crearTabla():
    conn = sqlite3.connect('alumnosdb.db',isolation_level=None)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS alumnos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido TEXT)")
    cursor.close()
    conn.close()

def insertarAlumno(nombre,apellido):
    conn = sqlite3.connect('alumnosdb.db', isolation_level=None)
    cursor = conn.cursor()
    query = "INSERT INTO alumnos (nombre,apellido) VALUES (?,?)"
    cursor.execute(query, (nombre, apellido))
    cursor.close()
    conn.close()

def buscarAlmnoNombre(nombre):
    conn = sqlite3.connect('alumnosdb.db', isolation_level=None)
    cursor = conn.cursor()
    query = "SELECT * FROM alumnos WHERE nombre = ?"
    cursor.execute(query, (nombre,))
    row = cursor.fetchall()
    cursor.close()
    conn.close()
    return row

def main1():
    #Este es el ejercicio como tal pero lo hare mas interactivo en el main
    crearTabla()
    insertarAlumno("Juan","Diez")
    insertarAlumno("Maria","Lopez")
    insertarAlumno("Pedro","Suarez")
    insertarAlumno("Roberto","Gomez")
    insertarAlumno("Aldo","Jimenez")
    insertarAlumno("Rogelio","Ambriz")
    insertarAlumno("Oscar","Perez")
    insertarAlumno("Luis","Hernandez")
    print(buscarAlmnoNombre("Pedro"))

def menu():
    print("1.- Crear tabla")
    print("2.- Insertar alumno")
    print("3.- Buscar alumno")
    print("4.- Salir")
    opcion = int(input("Elija una opción: "))
    return opcion

def main():
    opcion = menu()
    match opcion:
        case 1:
            crearTabla()
        case 2:
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            insertarAlumno(nombre,apellido)
        case 3:
            nombre = input("Nombre: ")
            print(buscarAlmnoNombre(nombre))
        case 4:
            print("Adios")
        case _:
            print("Opción no valida")