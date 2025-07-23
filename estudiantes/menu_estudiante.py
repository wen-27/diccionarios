from limpiar_pantalla import*
from agregar_estudiante import*
MAIN_MENU =  """
======================
MENU PRINCIPAL
======================

1. AGREGAR ESTUDIANTE
2. ELIMINAR ESTUDIANTE
3. MODIFICAR ESTUDIANTE
=======================

ingrese una opcion: 
"""



def main():
    while True:
        limpiar_pantalla()
        print(MAIN_MENU)
        try:
            opc = input(" = ")
            match opc:
                case "1":
                    limpiar_pantalla()
                    agregar_estudiante()
                    pausar_pantalla()
                case "2":
                    limpiar_pantalla()
                    pass
                    pausar_pantalla()
                case "3":
                    limpiar_pantalla()
                    pass
                    pausar_pantalla()
                    break
                case _:
                    print("ERROR...")
                    pausar_pantalla()
        except (ValueError):
            print("Error solo secuiionadnunerop)"
            "continue")



# Funcion principal
if __name__ == "__main__":
    main()