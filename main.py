import os
from modules import functions


# Este es el menú principal del programa
def mostar_menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("---BIENVEIDO---------------------")
    print("-----------------------------")
    print("1. Gestion de herramientas")
    print("2. Gestion de usuarios")
    print("3. gestion de prestamos")
    print("4.consulta y reporte de prestamos")
    print("5. registro de eventos")
    print("6. permisos a manejar")
    print("7. salir")



while True:
    functions.mostar_menu_principal()
        
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        functions.mostrar_menu_gestion_herramientas()
    elif opcion == 2:
        eliminar_herramienta()
    elif opcion == 3:
        modificar_herramienta()
    elif opcion == 4:
        consultar_herramienta()
    elif opcion == 5:
        listar_herramientas()
    elif opcion == 6:
        break
    else:
        print("Opción inválida, por favor intente de nuevo.")
