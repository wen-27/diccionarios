import os
import ui.rutas as rutas
import ui.rutas as main_menu_rutas
opcionesMenu = ['Administrar rutas','Administrar Campers','Gestion de Skills','Salir']

opcionesCampers = ['Crear camper','Editar camper','Eliminar camper','Listar campers','Salir']
opcionesSkills = ['Crear Skill','Editar Skill','Eliminar Skill','Listar Skill','Salir']
def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bienvenido al Menú Principal")
    for i, opcion in enumerate(opcionesMenu, start=1):
        print(f"{i}. {opcion}")
    try:
        op = int(input("Seleccione una opción: ")) - 1
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        input("Presione Enter para continuar...")
        return main_menu()
    if op < 0 or op >= len(opcionesMenu):
        print("Opción no válida. Intente de nuevo.")
        return main_menu()
    match op:
        case 0:  # Administrar rutas
            main_menu_rutas.main_menu_rutas()
            return main_menu()
        case 1:
            pass
        case 2:  # Gestion de Skills
            pass
        case 3:
            pass

def main_menu_campers()-> int:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bienvenido al Menú de Campers")
    for i, opcion in enumerate(opcionesCampers, start=1):
        print(f"{i}. {opcion}")
    try:
        op = int(input("Seleccione una opción: ")) - 1
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        input("Presione Enter para continuar...")
        return main_menu_campers()
    if op < 0 or op >= len(opcionesCampers):
        print("Opción no válida. Intente de nuevo.")
        return main_menu_campers()
    return op

def main_menu_skills()-> int:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bienvenido al Menú de Skills")
    for i, opcion in enumerate(opcionesSkills, start=1):
        print(f"{i}. {opcion}")
    try:
        op = int(input("Seleccione una opción: ")) - 1
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        input("Presione Enter para continuar...")
        return main_menu_skills()
    if op < 0 or op >= len(opcionesSkills):
        print("Opción no válida. Intente de nuevo.")
        return main_menu_skills()
    return op