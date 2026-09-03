==================================================
  SISTEMA COMUNITARIO DE PRÉSTAMO DE HERRAMIENTAS
==================================================
1. Iniciar Sesión
2. Salir
--------------------------------------------------
Seleccione una opción:


==================================================
             MENÚ DE ADMINISTRADOR
==================================================
1. Gestión de Herramientas (Agregar, Eliminar, Modificar, Buscar, Listar)
2. Gestión de Usuarios (Crear, Listar, Buscar, Actualizar, Eliminar)
3. Gestión de Préstamos y Solicitudes
   ├─ Aprobar / Rechazar Solicitudes
   ├─ Registrar Devolución
   └─ Consultar Préstamos Activos
4. Consultas y Reportes
   ├─ Herramientas con stock bajo (< 3)
   ├─ Préstamos activos y vencidos
   ├─ Historial de préstamos por usuario
   ├─ Herramientas más solicitadas
   └─ Usuarios con más solicitudes
5. Ver Registro de Eventos (Logs)
6. Cerrar Sesión
--------------------------------------------------
Seleccione una opción:


==================================================
               MENÚ DE RESIDENTE
==================================================
1. Consultar Herramientas Disponibles
2. Solicitar Préstamo de Herramienta
3. Ver Mis Solicitudes y Préstamos
4. Cerrar Sesión
--------------------------------------------------
Seleccione una opción:


import os, logging
from modulos import eventos, functions, herramientas, permisos, prestamos, usuarios

logging.info("Sistema iniciado correctamente.")
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
    

- si no hay prestamos activo mostrar mensaje de que no hay prestamos activos
- si no hay prestamos vencidos mostrar mensaje de que no hay prestamos vencidos
- hacer mas feito lo de herramientas amas pedidoas
- hacer mas feito lo de usuarios que mas piden

testtear fechas y cantidades

- **Usuario (Residente):**
  - Consulta el estado de las herramientas, su disponibilidad futura y quién la posee actualmente.
  - Crea solicitudes de herramientas *(que deben ser aprobadas por el administrador)*.
