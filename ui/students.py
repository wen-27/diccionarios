import datamodels.modelsdata as models
import os

def add_student():
    os.system('cls' if os.name == 'nt' else 'clear')

    student = models.students.copy()
    id = input("Ingrese el ID del Estudiante: ")
    student['nombre'] = input("Ingrese el Nombre del Estudiante: ")
    student['edad'] = int(input("Ingrese la Edad del Estudiante: "))
    student['email'] = input("Ingrese el Email del Estudiante: ")
    student['telefono'] = input("Ingrese el Telefono del Estudiante: ")
    models.campus.update({id: student})

def show_students():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Lista de Estudiantes:")
    for id, student in models.campus.items():
        print(f'ID: {id}, Nombre: {student['nombre']}, Edad: {student['edad']}, Email: {student['email']}, Telefono: {student['telefono']}')