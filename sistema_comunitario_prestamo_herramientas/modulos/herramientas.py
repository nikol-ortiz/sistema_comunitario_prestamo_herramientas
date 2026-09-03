import os

def mostrar_menu_gestion_herramientas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("gestion de herramientas")
    print("-----------------------------")
    print("1. agregar herramienta")
    # nombre, descripcion, cantidad, estado, categoria, fecha de adquisicion
    print("2. eliminar herramienta")
    print("3. modificar herramienta")
    print("4. consultar herramienta")
    print("5. listar herramientas")
    print("6. Volver al menu principal")
    opcion_gestion_herramientas = int(input("Seleccione una opción: "))

    if opcion_gestion_herramientas == 1:
        print('Agregar herramienta')
    elif opcion_gestion_herramientas == 2:
        print('Eliminar herramienta')
    elif opcion_gestion_herramientas == 3:
        print('Modificar herramienta')
    elif opcion_gestion_herramientas == 4:
        print('Consultar herramienta')
    elif opcion_gestion_herramientas == 5:
        print('Listar herramientas')
    elif opcion_gestion_herramientas == 6:
        print("Volver al menu principal")
    else:
        print("Opción inválida, por favor intente de nuevo.")
        
    input("Presione cualquier tecla para para continuar...")