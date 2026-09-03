import os, json
from datetime import datetime
import uuid


# Rutas de los archivos JSON
ruta_prestamos = "data/prestamos.json"
ruta_herramientas = "data/herramientas.json"

os.makedirs("data", exist_ok=True)

# Cargar datos de préstamos
if os.path.exists(ruta_prestamos):
    try:
        with open(ruta_prestamos, "r", encoding="utf-8") as f:
            prestamos = json.load(f)
    except json.decoder.JSONDecodeError:
        prestamos = []
else:
    prestamos = []


def cargar_herramientas():# cargar das de herramientas 
    if os.path.exists(ruta_herramientas):
        try:
            with open(ruta_herramientas, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.decoder.JSONDecodeError:
            return []
    return []

def guardar_herramientas(herramientas):#guardar datos de herramientas
    with open(ruta_herramientas, "w", encoding="utf-8") as f:
        json.dump(herramientas, f, ensure_ascii=False, indent=4)

def guardar_prestamos():
    with open(ruta_prestamos, "w", encoding="utf-8") as f:
        json.dump(prestamos, f, ensure_ascii=False, indent=4)


 # menu gestion de prestamos
def mostrar_menu_gestion_prestamos():
    opcion = 0
    while opcion != 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------")
        print("     GESTIÓN DE PRÉSTAMOS    ")
        print("-----------------------------")
        print("1. Registrar nuevo préstamo")
        print("2. Registrar devolución de herramienta")
        print("3. Consultar préstamo")
        print("4. Listar préstamos")
        print("5. Aprobar/Rechazar préstamos")
        print("6. Volver al menú principal")
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            input("Presione Enter para continuar...")
            continue

        if opcion == 1:
            registrar_prestamo()
        elif opcion == 2:
            registrar_devolucion()
        elif opcion == 3:
            consultar_prestamo()
        elif opcion == 4:
            listar_prestamos()
        elif opcion == 5:
            aprovar_prestamos()
        elif opcion == 6:
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")


#  FUNCIONES DEL MÓDULO 

def registrar_prestamo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("      REGISTRAR PRÉSTAMO     ")
    print("-----------------------------")
    
    herramientas = cargar_herramientas()
    if not herramientas:
        print("No hay herramientas registradas en el sistema.")
        input("Presione Enter para continuar...")
        return

    usar_random = input("¿Desea generar un ID de préstamo aleatorio? (s/n): ").strip().lower()
    if usar_random == 's':
        id_prestamo = str(uuid.uuid4())[:8]  # Generate short random ID
        print(f"ID de préstamo generado: {id_prestamo}")
    else:
        id_prestamo = input("Ingrese el ID del préstamo: ")
    
    # Validar que no se repita el ID del préstamo
    for p in prestamos:
        if p["id_prestamo"] == id_prestamo:
            print("Error: Ya existe un préstamo con ese ID.")
            input("Presione Enter para continuar...")
            return

    ver_usuarios = input("¿Desea ver la lista de usuarios antes de ingresar el ID? (s/n): ").strip().lower()
    if ver_usuarios == 's':
        from modulos.usuarios import listar_usuarios
        listar_usuarios()

    usuario_id = input("Ingrese el ID del usuario: ")
    
    ver_herramientas = input("¿Desea ver la lista de herramientas antes de ingresar el ID? (s/n): ").strip().lower()
    if ver_herramientas == 's':
        from modulos.herramientas import listar_herramientas
        listar_herramientas()

    try:
        herramienta_id = int(input("Ingrese el ID de la herramienta: "))
    except ValueError:
        print("Error: El ID de la herramienta debe ser un número.")
        input("Presione Enter para continuar...")
        return

    # Buscar la herramienta para validar stock
    herramienta_encontrada = None
    for h in herramientas:
        if str(h.get("id")) == str(herramienta_id):
            herramienta_encontrada = h
            break

    if not herramienta_encontrada:
        print("Error: La herramienta especificada no existe.")
        input("Presione Enter para continuar...")
        return

    # REGLA DE NEGOCIO: Verificar si hay stock disponible antes de continuar
    stock_actual = herramienta_encontrada.get("cantidad_disponible", 0)
    if stock_actual <= 0:
        print(f"Error: No hay unidades disponibles de {herramienta_encontrada.get('nombre', 'la herramienta')}.")
        input("Presione Enter para continuar...")
        return

    try:
        cantidad = int(input(f"Ingrese la cantidad a prestar (Disponible: {stock_actual}): "))
    except ValueError:
        print("Error: La cantidad debe ser un número entero.")
        input("Presione Enter para continuar...")
        return

    # REGLA DE NEGOCIO 1: Verificar stock disponible
    if cantidad <= 0:
        print("Error: La cantidad debe ser mayor a cero.")
        input("Presione Enter para continuar...")
        return

    if cantidad > stock_actual:
        print(f"Error: Stock insuficiente. Solo hay {stock_actual} unidades disponibles.")
        input("Presione Enter para continuar...")
        return

    fecha_inicio = input("Ingrese fecha de inicio (AAAA-MM-DD) [Enter para fecha actual]: ")
    if not fecha_inicio.strip():
        fecha_inicio = datetime.now().strftime("%Y-%m-%d")

    fecha_estimada_devolucion = input("Ingrese fecha estimada de devolución (AAAA-MM-DD): ")
    observaciones = input("Observaciones adicionales: ")

    # REGLA DE NEGOCIO 
    herramienta_encontrada["cantidad_disponible"] -= cantidad
    guardar_herramientas(herramientas)

    # Crear el diccionario del préstamo
    nuevo_prestamo = {
        "id_prestamo": id_prestamo,
        "usuario_id": usuario_id,
        "herramienta_id": herramienta_id,
        "cantidad": cantidad,
        "fecha_inicio": fecha_inicio,
        "fecha_estimada_devolucion": fecha_estimada_devolucion,
        "estado": "aprobado",
        "observaciones": observaciones
    }

    prestamos.append(nuevo_prestamo)
    guardar_prestamos()

    print("\n¡Préstamo registrado exitosamente y stock actualizado!")
    input("Presione Enter para continuar...")


def registrar_devolucion():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("    REGISTRAR DEVOLUCIÓN     ")
    print("-----------------------------")

    quiere_listar = input("¿Desea ver la lista de préstamos? (s/n)  ").strip().lower()
    if quiere_listar == 's':
        listar_prestamos()
               
    id_prestamo = input("Ingrese el ID del préstamo a devolver: ")
    prestamo_encontrado = None

    for p in prestamos:
        if p["id_prestamo"] == id_prestamo:
            prestamo_encontrado = p
            break

    if not prestamo_encontrado:
        print("Error: Préstamo no encontrado.")
        input("Presione Enter para continuar...")
        return

    if prestamo_encontrado["estado"] == "devuelto":
        print("Este préstamo ya fue devuelto anteriormente.")
        input("Presione Enter para continuar...")
        return

    # REGLA DE NEGOCIO 2: Restaurar stock de la herramienta
    herramientas = cargar_herramientas()
    for h in herramientas:
        if str(h.get("id")) == str(prestamo_encontrado["herramienta_id"]):
            h["cantidad_disponible"] = h.get("cantidad_disponible", 0) + prestamo_encontrado["cantidad"]
            break

    guardar_herramientas(herramientas)

    # Registrar la hora de entrega
    usar_actual = input("¿Desea registrar la fecha y hora actual para la devolución? (s/n): ").strip().lower()
    if usar_actual == 's':
        fecha_devolucion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        fecha_devolucion = input("Ingrese la fecha y hora de devolución (AAAA-MM-DD HH:MM:SS): ")

    # Actualizar estado del préstamo
    prestamo_encontrado["estado"] = "devuelto"
    prestamo_encontrado["fecha_devolucion_real"] = fecha_devolucion
    guardar_prestamos()

    print(f"\n¡Devolución registrada exitosamente el {fecha_devolucion} y stock restaurado!")
    input("Presione Enter para continuar...")


def consultar_prestamo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("      CONSULTAR PRÉSTAMO     ")
    print("-----------------------------")
    
    id_prestamo = input("Ingrese el ID del préstamo: ")
    encontrado = False

    for p in prestamos:
        if p["id_prestamo"] == id_prestamo:
            print("\n--- Detalles del Préstamo ---")
            print(f"ID Préstamo: {p['id_prestamo']}")
            print(f"ID Usuario: {p['usuario_id']}")
            print(f"ID Herramienta: {p['herramienta_id']}")
            print(f"Cantidad: {p['cantidad']}")
            print(f"Fecha Inicio: {p['fecha_inicio']}")
            print(f"Fecha Estimada Devolución: {p['fecha_estimada_devolucion']}")
            print(f"Estado: {p['estado']}")
            if p.get("fecha_devolucion_real"):
                print(f"Fecha Devolución Real: {p['fecha_devolucion_real']}")
            print(f"Observaciones: {p['observaciones']}")
            encontrado = True
            break

    if not encontrado:
        print("Préstamo no encontrado.")
    
    input("\nPresione Enter para continuar...")


def listar_prestamos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("     LISTA DE PRÉSTAMOS      ")
    print("-----------------------------")

    if not prestamos:
        print("No hay préstamos registrados.")
    else:
        for p in prestamos:
            print(f"ID: {p['id_prestamo']} | User: {p['usuario_id']} | Tool: {p['herramienta_id']} | Cant: {p['cantidad']} | Estado: {p['estado']}")

    input("\nPresione Enter para continuar...")

def aprovar_prestamos():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------")
        print("   APROBAR/RECHAZAR PRÉSTAMOS")
        print("-----------------------------")

        if not prestamos:
            print("No hay préstamos registrados.")
            input("\nPresione Enter para volver...")
            break

        # Filtrar solo préstamos pendientes
        pendientes = [p for p in prestamos if p["estado"] == "pendiente"]
        
        if not pendientes:
            print("No hay préstamos pendientes de aprobación.")
            input("\nPresione Enter para volver...")
            break

        print(f"Hay {len(pendientes)} préstamos pendientes.")

        quiere_listar = input("¿Desea ver la lista de préstamos pendientes? (s/n) [n para continuar, q para salir]: ").strip().lower()
        if quiere_listar == 'q':
            break
        if quiere_listar == 's':
            print("\n--- Préstamos Pendientes ---")
            for p in pendientes:
                print(f"ID: {p['id_prestamo']} | User: {p['usuario_id']} | Tool: {p['herramienta_id']} | Cant: {p['cantidad']}")
           
        id_prestamo = input("\nIngrese el ID del préstamo a gestionar (o 'salir' para volver): ").strip()
        if id_prestamo.lower() == 'salir':
            break

        prestamo_encontrado = None
        for p in prestamos:
            if p["id_prestamo"] == id_prestamo:
                prestamo_encontrado = p
                break

        if not prestamo_encontrado:
            print(f"Error: Préstamo con ID '{id_prestamo}' no encontrado.")
            input("Presione Enter para intentar de nuevo...")
            continue

        if prestamo_encontrado["estado"] != "pendiente":
            print(f"El préstamo '{id_prestamo}' no está en estado 'pendiente' (Estado actual: {prestamo_encontrado['estado']}).")
            input("Presione Enter para continuar...")
            continue

        print(f"\nGestionando préstamo: {id_prestamo}")
        accion = input("¿Desea (A)probar o (R)echazar este préstamo? (a/r): ").strip().lower()

        if accion == 'a':
            # REGLA DE NEGOCIO: Al aprobar, debemos restar el stock
            herramientas = cargar_herramientas()
            herramienta_id = prestamo_encontrado["herramienta_id"]
            cantidad = prestamo_encontrado["cantidad"]
            
            herramienta_encontrada = None
            for h in herramientas:
                if str(h.get("id")) == str(herramienta_id):
                    herramienta_encontrada = h
                    break
            
            if not herramienta_encontrada:
                print("Error: La herramienta asociada al préstamo no existe.")
                input("Presione Enter para continuar...")
                continue
                
            if herramienta_encontrada.get("cantidad_disponible", 0) < cantidad:
                print(f"Error: No hay stock suficiente para aprobar este préstamo. Disponible: {herramienta_encontrada.get('cantidad_disponible')}")
                input("Presione Enter para continuar...")
                continue

            # Restar stock
            herramienta_encontrada["cantidad_disponible"] -= cantidad
            guardar_herramientas(herramientas)

            # Actualizar estado del préstamo
            prestamo_encontrado["estado"] = "aprobado"
            guardar_prestamos()
            print(f"\n¡Préstamo '{id_prestamo}' APROBADO exitosamente y stock actualizado!")

        elif accion == 'r':
            motivo = input("Ingrese el motivo del rechazo (opcional): ").strip()
            prestamo_encontrado["estado"] = "rechazado"
            if motivo:
                prestamo_encontrado["observaciones"] = f"RECHAZADO: {motivo} | " + prestamo_encontrado.get("observaciones", "")
            
            guardar_prestamos()
            print(f"\n¡Préstamo '{id_prestamo}' RECHAZADO exitosamente!")
        else:
            print("Acción cancelada. Opción no válida.")

        otra = input("\n¿Desea gestionar otro préstamo? (s/n): ").strip().lower()
        if otra != 's':
            break