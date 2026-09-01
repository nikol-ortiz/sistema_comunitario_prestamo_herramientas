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
    print("6. salir")
    opcion_gestion_herramientas = int(input("Seleccione una opción: "))