import os, logging
from modulos import herramientas, usuarios, prestamos, eventos, consultas_reportes
from modulos_usuario import consultar_herraminetas, solicitud_prestamo, historial
import login

# --- MENÚS ---

def mostrar_menu_admin(nombre_admin):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==================================================")
    print(f"       MENÚ DE ADMINISTRADOR - [{nombre_admin}]")
    print("==================================================")
    print("1. Gestión de Herramientas")
    print("2. Gestión de Usuarios")
    print("3. Gestión de Préstamos y Solicitudes")
    print("4. Consultas y Reportes")
    print("5. Ver Registro de Eventos (Logs)")
    print("6. Cerrar Sesión")
    print("--------------------------------------------------")

def mostrar_menu_residente(nombre_usuario):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==================================================")
    print(f"         MENÚ DE RESIDENTE - [{nombre_usuario}]")
    print("==================================================")
    print("1. Consultar Herramientas Disponibles")
    print("2. Solicitar Préstamo de Herramienta")
    print("3. Ver Mis Solicitudes y Préstamos")
    print("4. Cerrar Sesión")
    print("--------------------------------------------------")


# --- Flujo de sesión ---

def flujo_administrador(usuario_actual):
    opcion = 0
    while opcion != 6:
        mostrar_menu_admin(usuario_actual['nombre'])
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            input("Presione Enter para continuar...")
            continue

        if opcion == 1:
            herramientas.mostrar_menu_gestion_herramientas()
        elif opcion == 2:
            usuarios.mostrar_menu_gestion_usuarios()
        elif opcion == 3:
            prestamos.mostrar_menu_gestion_prestamos()
        elif opcion == 4:
            consultas_reportes.mostrar_menu_consultas_reportes()
        elif opcion == 5:
            eventos.ver_registro_eventos()
        elif opcion == 6:
            print("Cerrando sesión de Administrador...")
            logging.info(f"Admin {usuario_actual['nombre']} cerró sesión.")
            input("Presione Enter para continuar...")
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")

def flujo_residente(usuario_actual):
    opcion = 0
    while opcion != 4:
        mostrar_menu_residente(usuario_actual['nombre'])
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            input("Presione Enter para continuar...")
            continue

        if opcion == 1:
            consultar_herraminetas.consultar_herramientas()
        elif opcion == 2:
            solicitud_prestamo.solicitar_prestamo(usuario_actual)
        elif opcion == 3:
            historial.ver_mi_historial(usuario_actual)
        elif opcion == 4:
            print("Cerrando sesión...")
            logging.info(f"Residente {usuario_actual['nombre']} cerró sesión.")
            input("Presione Enter para continuar...")
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")


# --- CICLO PRINCIPAL ---

def main():
    opcion_main = 0
    while opcion_main != 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('==================================================')
        print('  SISTEMA COMUNITARIO DE PRÉSTAMO DE HERRAMIENTAS  ')
        print('==================================================')
        print('1. Iniciar Sesión')
        print('2. Salir')
        print('--------------------------------------------------')
        
        try:
            opcion_main = int(input('Ingrese una opción: '))
        except ValueError:
            print("Por favor ingrese un número válido.")
            input("Presione Enter para continuar...")
            continue

        if opcion_main == 1:
            usuario_logueado = login.iniciar_sesion()
            
            if usuario_logueado is not None:
                # Verificamos el tipo de usuario 
                es_admin = usuario_logueado.get('tipo_de_usuario') in [True]
                
                if es_admin:
                    flujo_administrador(usuario_logueado)
                else:
                    flujo_residente(usuario_logueado)

        elif opcion_main == 2:
            print('¡Hasta luego!')
            input("Presione Enter para continuar...")
        else:
            print('Opción inválida...')
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()