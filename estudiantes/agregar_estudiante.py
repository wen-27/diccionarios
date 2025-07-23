from ui.students import*
from limpiar_pantalla import*

def agregar_estudiante(id, nombre, edad):
    if id in add_student:
        print("El estudiante ya existe.")
    else:
        add_student[id] = {"nombre": nombre, "edad": edad}
        print("Estudiante agregado correctamente.")

def modificar_estudiante(id, nuevo_nombre=None, nueva_edad=None):
    if id in add_student:
        if nuevo_nombre:
            add_student[id]["nombre"] = nuevo_nombre
        if nueva_edad:
            add_student[id]["edad"] = nueva_edad
        print("Estudiante modificado correctamente.")
    else:
        print("El estudiante no existe.")

def eliminar_estudiante(id):
    if id in add_student:
        del add_student[id]
        print("Estudiante eliminado correctamente.")
    else:
        print("El estudiante no existe.")

def mostrar_estudiantes():
    if add_student:
        for id, datos in add_student.items():
            print(f"ID: {id} | Nombre: {datos['nombre']} | Edad: {datos['edad']}")
    else:
        print("No hay estudiantes registrados.")
