import json
import os

# Consulta el estado de las herramientas, su disponibilidad futura y quién la posee actualmente.
def consultar_herramientas():
    # Rutas de los archivos
    ruta_herramientas = "data/herramientas.json"
    ruta_prestamos = "data/prestamos.json"
    ruta_usuarios = "data/usuarios.json"

    # Limpiar pantalla
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==================================================")
    print("       CONSULTA DE HERRAMIENTAS")
    print("==================================================")

    # Cargar datos de herramientas
    herramientas = []
    if os.path.exists(ruta_herramientas):
        try:
            with open(ruta_herramientas, "r", encoding="utf-8") as f:
                herramientas = json.load(f)
        except:
            herramientas = []

    # Cargar datos de préstamos
    prestamos = []
    if os.path.exists(ruta_prestamos):
        try:
            with open(ruta_prestamos, "r", encoding="utf-8") as f:
                prestamos = json.load(f)
        except:
            prestamos = []

    # Cargar datos de usuarios
    usuarios = []
    if os.path.exists(ruta_usuarios):
        try:
            with open(ruta_usuarios, "r", encoding="utf-8") as f:
                usuarios = json.load(f)
        except:
            usuarios = []

    if not herramientas:
        print("No hay herramientas registradas en el sistema.")
    else:
        for h in herramientas:
            print(f"\nID: {h.get('id', 'N/A')}")
            print(f"Nombre: {h.get('nombre', 'N/A')}")
            print(f"Categoría: {h.get('categoria', 'N/A')}")
            
            # Determinar el texto del estado
            estado_num = h.get('estado', 0)
            if estado_num == 1:
                estado_texto = "Activa"
            elif estado_num == 2:
                estado_texto = "En reparación"
            elif estado_num == 3:
                estado_texto = "Fuera de servicio"
            else:
                estado_texto = "Desconocido"
            
            print(f"Estado: {estado_texto}")
            print(f"Cantidad en inventario: {h.get('cantidad_disponible', 0)}")

            # Buscar quién tiene la herramienta actualmente
            prestamos_activos = False
            for p in prestamos:
                # Consideramos préstamos "aprobados" como los que están actualmente fuera
                if str(p.get('herramienta_id')) == str(h.get('id')) and p.get('estado') == "aprobado":
                    if not prestamos_activos:
                        print("Préstamos actuales:")
                        prestamos_activos = True
                    
                    # Buscar el nombre del usuario que tiene la herramienta
                    nombre_usuario = "Usuario desconocido"
                    for u in usuarios:
                        if str(u.get('id')) == str(p.get('usuario_id')):
                            nombre_usuario = f"{u.get('nombre', '')} {u.get('apellido', '')}"
                            break
                    
                    print(f"  - Poseído por: {nombre_usuario} (ID: {p.get('usuario_id')})")
                    print(f"    Cantidad prestada: {p.get('cantidad')}")
                    print(f"    Fecha de devolución esperada: {p.get('fecha_estimada_devolucion')}")
            
            if not prestamos_activos:
                print("No hay préstamos activos para esta herramienta.")
            
            print("-------------------------------------")

    print("\n")
    input("Presione Enter para continuar...")



