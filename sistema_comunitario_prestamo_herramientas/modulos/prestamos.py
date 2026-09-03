import os
import json
from datetime import datetime

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
    while opcion != 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------")
        print("     GESTIÓN DE PRÉSTAMOS    ")
        print("-----------------------------")
        print("1. Registrar nuevo préstamo")
        print("2. Registrar devolución de herramienta")
        print("3. Consultar préstamo")
        print("4. Listar préstamos")
        print("5. Volver al menú principal")
        
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

    id_prestamo = input("Ingrese el ID del préstamo: ")
    
    # Validar que no se repita el ID del préstamo
    for p in prestamos:
        if p["id_prestamo"] == id_prestamo:
            print("Error: Ya existe un préstamo con ese ID.")
            input("Presione Enter para continuar...")
            return

    usuario_id = input("Ingrese el ID del usuario: ")
    herramienta_id = input("Ingrese el ID de la herramienta: ")

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

    try:
        cantidad = int(input(f"Ingrese la cantidad a prestar (Disponible: {herramienta_encontrada.get('stock', 0)}): "))
    except ValueError:
        print("Error: La cantidad debe ser un número entero.")
        input("Presione Enter para continuar...")
        return

    # REGLA DE NEGOCIO 1: Verificar stock disponible
    stock_actual = herramienta_encontrada.get("stock", 0)
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
    herramienta_encontrada["stock"] -= cantidad
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
            h["stock"] = h.get("stock", 0) + prestamo_encontrado["cantidad"]
            break

    guardar_herramientas(herramientas)

    # Actualizar estado del préstamo
    prestamo_encontrado["estado"] = "devuelto"
    guardar_prestamos()

    print("\n¡Devolución registrada exitosamente y stock restaurado!")
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