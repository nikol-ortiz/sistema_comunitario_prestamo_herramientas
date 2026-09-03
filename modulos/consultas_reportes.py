# ### 4. Consultas y Reportes

# - Herramientas con stock bajo *(menos de 3 unidades)*.
# - Préstamos activos y vencidos.
# - Historial de préstamos de un usuario específico.
# - Herramientas más solicitadas por la comunidad.
# - Usuarios que más herramientas han solicitado.

# ###
import os
import json
from datetime import datetime

def mostrar_menu_consultas_reportes():
    opcion = 0
    while opcion != 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==================================================")
        print("       MENÚ DE CONSULTAS Y REPORTES")
        print("==================================================")
        print("1. Herramientas con stock bajo")
        print("2. Préstamos activos y vencidos")
        print("3. Historial de préstamos de un usuario específico")
        print("4. Herramientas más solicitadas por la comunidad")
        print("5. Usuarios que más herramientas han solicitado")
        print("6. Volver al Menú Principal")
        print("--------------------------------------------------")
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            input("Presione Enter para continuar...")
            continue
        
        if opcion == 1:
            consultar_herramientas_stock_bajo()
        elif opcion == 2:
            consultar_prestamos_activos_vencidos()
        elif opcion == 3:
            historial_prestamos_usuario()
        elif opcion == 4:
            herramientas_mas_solicitadas()
        elif opcion == 5:
            usuarios_que_mas_solicitan()
        elif opcion == 6:
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")

def consultar_herramientas_stock_bajo():
    from modulos.prestamos import cargar_herramientas
    herramientas = cargar_herramientas()
    print("\n Herramientas con poco stock (menos de 3)")
    encontrado = False
    for herramienta in herramientas:
        if herramienta.get("cantidad_disponible", 0) < 3:
            print(f"ID: {herramienta.get('id')}  Nombre: {herramienta.get('nombre')}  Stock: {herramienta.get('cantidad_disponible')}")
            encontrado = True
    
    if not encontrado:
        print("No se encontraron herramientas con stock bajo.")
    
    input("\nPresione Enter para continuar  ")

def consultar_prestamos_activos_vencidos():
    from modulos.prestamos import prestamos
    print("\n¿Qué reporte deseas ver?")
    print("1. Préstamos Activos (Los que están aprobados)")
    print("2. Préstamos Vencidos (Ya pasó la fecha de entrega)")
    
    que_quiere_ver = input("Seleccione (1 o 2): ")
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    
    if que_quiere_ver == "1":
        print("\n Listado de Préstamos Activos")
        encontrado = False
        for p in prestamos:
            if p["estado"] == "aprobado":
                print(f"ID: {p.get('id_prestamo')} | Usuario: {p.get('usuario_id')} | Herramienta: {p.get('herramienta_id')} | Entrega: {p.get('fecha_estimada_devolucion')}")
                encontrado = True
        if not encontrado:
            print("No se encontraron préstamos activos.")
    
    elif que_quiere_ver == "2":
        print("\n Listado de Préstamos Vencidos")
        encontrado = False
        for p in prestamos:
            if p["estado"] == "aprobado" and p["fecha_estimada_devolucion"] < fecha_actual:
                print(f"ID: {p.get('id_prestamo')} | Usuario: {p.get('usuario_id')} | Herramienta: {p.get('herramienta_id')} | Vencía: {p.get('fecha_estimada_devolucion')}")
                encontrado = True
        if not encontrado:
            print("No se encontraron préstamos vencidos.")
    else:
        print("Opción no válida.")
        
    input("\nPresione Enter para continuar...")

def historial_prestamos_usuario():
    from modulos.prestamos import prestamos
    
    quiere_ver_usuarios = input("¿Desea ver la lista de usuarios primero? (s/n): ").lower()
    if quiere_ver_usuarios == "s":
        try:
            from modulos.usuarios import listar_usuarios
            listar_usuarios()
        except ImportError:
            print("No se pudo cargar la lista de usuarios.")
            
    el_id_usuario = input("Ingrese el ID del usuario para ver su historial: ")
    print(f"\n--- Historial de préstamos del usuario {el_id_usuario} ---")
    
    hay_prestamos = False
    for p in prestamos:
        if str(p["usuario_id"]) == str(el_id_usuario):
            print(f"ID Préstamo: {p.get('id_prestamo')} | Herramienta: {p.get('herramienta_id')} | Cant: {p.get('cantidad')} | Estado: {p.get('estado')}")
            hay_prestamos = True
            
    if not hay_prestamos:
        print("Este usuario no tiene préstamos registrados.")
        
    input("\nPresione Enter para continuar...")

def herramientas_mas_solicitadas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--------------------------------------------------")
    print("      HERRAMIENTAS MÁS PEDIDAS POR LA GENTE")
    print("--------------------------------------------------")
    
    from modulos.prestamos import prestamos
    from modulos.prestamos import cargar_herramientas
    
    if not prestamos:
        print("Todavía no hay préstamos en el sistema.")
        input("\nPresione Enter para continuar...")
        return

    el_conteo = {}
    for p in prestamos:
        id_h = str(p.get("herramienta_id"))
        if id_h in el_conteo:
            el_conteo[id_h] = el_conteo[id_h] + 1
        else:
            el_conteo[id_h] = 1

    las_herramientas = cargar_herramientas()
    nombres_h = {}
    for h in las_herramientas:
        nombres_h[str(h.get("id"))] = h.get("nombre")

    # Ordenamos de mayor a menor
    lista_ordenada = sorted(el_conteo.items(), key=lambda x: x[1], reverse=True)

    print("Herramienta       Cantidad de veces pedida")
    print("--------------------------------------------------")
    for id_h, total in lista_ordenada:
        nombre = nombres_h.get(id_h, f"ID: {id_h}")
        print(f"{nombre}       {total} veces")

    input("\nPresione Enter para continuar...")

def usuarios_que_mas_solicitan():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--------------------------------------------------")
    print("      USUARIOS QUE MÁS PIDEN HERRAMIENTAS")
    print("--------------------------------------------------")
    
    from modulos.prestamos import prestamos
    from modulos.usuarios import usuarios
    
    if not prestamos:
        print("No hay registros de préstamos para mostrar.")
        input("\nPresione Enter para continuar...")
        return

    conteo_user = {}
    for p in prestamos:
        id_u = str(p.get("usuario_id"))
        if id_u in conteo_user:
            conteo_user[id_u] = conteo_user[id_u] + 1
        else:
            conteo_user[id_u] = 1

    nombres_u = {}
    for u in usuarios:
        nombres_u[str(u.get("id"))] = u.get("nombre")

    orden_usuarios = sorted(conteo_user.items(), key=lambda x: x[1], reverse=True)

    print("Usuario              Total de préstamos")
    print("--------------------------------------------------")
    for id_u, total in orden_usuarios:
        nombre = nombres_u.get(id_u, f"ID: {id_u}")
        print(f"{nombre}       {total} herramientas")

    input("\nPresione Enter para continuar...")
