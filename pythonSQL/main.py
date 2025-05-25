import dbManager as bm

bd = bm.baseDatos(ruta = "./", bd = "miBD.sqlite3")

def ingresarDatos(Cadena):
    retorno = input(Cadena)
    return retorno

def seleccionarOpcion():
    opcion = ingresarDatos("1-Agregar alumno\n2-Eliminar alumno\n3-Modificar \
calificiones\n4-Mostrar alumnos\n5-Crear base de datos\n6-Salir\n")
    return opcion

def agregarAlumno():
    print("Agregando alumno\n")
    nombre = ingresarDatos("Ingrese el nombre del alumno a registrar: ")
    bd.agregarAlumno(nombre)
    
def eliminarAlumno():
    print("Eliminando alumno\n")
    nombre = ingresarDatos("Ingrese el nombre del alumno a eliminar: ")
    bd.eliminarAlumno(nombre)

def modificarCalificaciones():
    print("Seleccione la materia a modificar: \n")
    materia = ingresarDatos("1-Espanol\n2-Matematicas\n3-Historia\n4-Regresar")
    
    if materia.isdigit():
        materia = int(materia)
        
        if materia == 1:
            nombre = ingresarDatos("Ingrese el nombre del alumno a modificar: ")
            calificacion = ingresarDatos("Ingrese la calificacion de espanol: ")
            lista = bd.actualizarEspanol(float(calificacion), nombre)
            
            for elemento in lista:
                print(elemento[0], elemento[1], elemento[2], elemento[3])
            print("\n")
        
        elif materia == 2:
            nombre = ingresarDatos("Ingrese el nombre del alumno a modificar: ")
            calificacion = ingresarDatos("Ingrese la calificacion de matematicas: ")
            lista = bd.actualizarMatematicas(float(calificacion), nombre)
            for elemento in lista:
                print(elemento[0], elemento[1], elemento[2], elemento[3])
            print("\n")
        
        elif materia == 3:
            nombre = ingresarDatos("Ingrese el nombre del alumno a modificar: ")
            calificacion = ingresarDatos("Ingrese la calificacion de historia: ")
            lista = bd.actualizarHistoria(float(calificacion), nombre)
            for elemento in lista:
                print(elemento[0], elemento[1], elemento[2], elemento[3])
            print("\n")
            
        elif materia == 4:
            pass
            
        else:
            print("Opcion no valida")
        
    else:
        print("Ingrese solo datos numericos")

def mostrarAlumnos():
    lista = bd.listarGeneral()
    for elemento in lista:
        print(elemento[0], elemento[1], elemento[2], elemento[3])
    print("\n")
    
def crearBD():
    bd.crearDB()
    

while True:
    print("Selecciona la opcion deseada: \n")
    
    opcion = seleccionarOpcion()
    
    if opcion.isdigit():
        opcion = int(opcion)
        
        if opcion == 1:
            agregarAlumno()
            
        elif opcion == 2:
            eliminarAlumno()
            
        elif opcion == 3:
            modificarCalificaciones()
        
        elif opcion == 4:
            mostrarAlumnos()
        
        elif opcion == 5:
            crearBD()
        
        elif opcion == 6:
            break
        
        else:
            print("Opcion no valida")
    
    else:
        print("Ingrese solo valores numericos")
    
    