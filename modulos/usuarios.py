# Operaciones: crear, listar, buscar, actualizar y eliminar usuarios.
import os

def mostrar_menu_gestion_usuarios():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("gestion de usuarios")
    print("-----------------------------")
    print("1. agregar usuario")
    print("2. eliminar usuario")
    print("3. modificar usuario")
    print("4. consultar usuario")
    print("5. listar usuarios")
    print("6. Volver al menu principal")
    opcion_gestion_usuarios = int(input("Seleccione una opción: "))

    if opcion_gestion_usuarios == 1:
        print('Agregar usuario')
    elif opcion_gestion_usuarios == 2:
        print('Eliminar usuario')
    elif opcion_gestion_usuarios == 3:
        print('Modificar usuario')
    elif opcion_gestion_usuarios == 4:
        print('Consultar usuario')
    elif opcion_gestion_usuarios == 5:
        print('Listar usuarios')
    elif opcion_gestion_usuarios == 6:
        print("Volver al menu principal")
    else:
        print("Opción invalida")
