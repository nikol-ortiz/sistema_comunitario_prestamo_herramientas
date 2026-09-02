import os
from modulos import eventos, functions, herramientas, permisos, prestamos, usuarios


# Este es el menú principal del programa
def mostar_menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("---BIENVEIDO---------------------")
    print("-----------------------------")
    print("1. Gestion de herramientas")
    print("2. Gestion de usuarios")
    print("3. gestion de prestamos")
    print("4. consulta y reporte de prestamos")
    print("5. registro de eventos")
    print("6. permisos a manejar")
    print("7. salir")


opcion = 0
while opcion != 7:
    mostar_menu_principal()
        
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        herramientas.mostrar_menu_gestion_herramientas()
    elif opcion == 2:
        usuarios.mostrar_menu_gestion_usuarios()
    elif opcion == 3:
        print('Gestion de prestamos')
    elif opcion == 4:
        print('Gestion de consulta y reporte de prestamos')
    elif opcion == 5:
        print('Gestion de registro de eventos')
    elif opcion == 6:
        print('Gestion de permisos a manejar')
    elif opcion == 7:
        print("Gracias por utilizar el sistema.")
    else:
        print("Opción inválida, por favor intente de nuevo.")
    

