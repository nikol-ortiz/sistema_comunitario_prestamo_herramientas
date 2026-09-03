import os
from datetime import datetime
import uuid
from modulos.prestamos import prestamos, guardar_prestamos, cargar_herramientas
from modulos.herramientas import listar_herramientas_disponibles
from modulos.functions import leer_entero, leer_fecha

def solicitar_prestamo(usuario_actual):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------------------")
    print("      SOLICITAR PRÉSTAMO DE HERRAMIENTA  ")
    print("-----------------------------------------")
    
    herramientas = cargar_herramientas()
    if not herramientas:
        print("No hay herramientas registradas en el sistema.")
        input("Presione Enter para continuar...")
        return

    # Listar solo las herramientas disponibles para préstamo
    listar_herramientas_disponibles()

    herramienta_id = leer_entero("\nIngrese el ID de la herramienta que desea solicitar: ")

    # Buscar la herramienta
    herramienta_encontrada = None
    for h in herramientas:
        if h.get("id") == herramienta_id:
            herramienta_encontrada = h
            break

    if not herramienta_encontrada:
        print("Error: La herramienta especificada no existe.")
        input("Presione Enter para continuar...")
        return

    # REGLA DE NEGOCIO: solo se prestan herramientas en estado 'Activa/Disponible' (1)
    if herramienta_encontrada.get("estado") != 1:
        print(f"Error: La herramienta '{herramienta_encontrada.get('nombre', 'seleccionada')}' no está disponible actualmente. Solo se prestan herramientas en estado 'Activa/Disponible'.")
        input("Presione Enter para continuar...")
        return

    stock_actual = herramienta_encontrada.get("cantidad_disponible", 0)
    if stock_actual <= 0:
        print(f"Error: No hay unidades disponibles de {herramienta_encontrada.get('nombre', 'la herramienta')}.")
        input("Presione Enter para continuar...")
        return

    cantidad = leer_entero(f"Ingrese la cantidad a solicitar (Disponible: {stock_actual}): ")

    if cantidad <= 0:
        print("Error: La cantidad debe ser mayor a cero.")
        input("Presione Enter para continuar...")
        return

    if cantidad > stock_actual:
        print(f"Error: Stock insuficiente. Solo hay {stock_actual} unidades disponibles.")
        input("Presione Enter para continuar...")
        return

    fecha_estimada_devolucion = leer_fecha("Ingrese fecha estimada de devolución (AAAA-MM-DD): ")
    observaciones = input("Motivo o comentarios de la solicitud: ")

    id_prestamo = str(uuid.uuid4())[:8]
    fecha_inicio = datetime.now().strftime("%Y-%m-%d")

    # Crear la solicitud con estado "pendiente"
    # No restamos stock todavía, se restará al aprobar
    nueva_solicitud = {
        "id_prestamo": id_prestamo,
        "usuario_id": usuario_actual["id"],
        "herramienta_id": herramienta_id,
        "cantidad": cantidad,
        "fecha_inicio": fecha_inicio,
        "fecha_estimada_devolucion": fecha_estimada_devolucion,
        "estado": "pendiente",
        "observaciones": observaciones
    }

    prestamos.append(nueva_solicitud)
    guardar_prestamos()

    print(f"\n¡Solicitud '{id_prestamo}' creada exitosamente con estado 'pendiente'!")
    print("Un administrador debe aprobar esta solicitud para que el préstamo sea efectivo.")
    input("Presione Enter para continuar...")
