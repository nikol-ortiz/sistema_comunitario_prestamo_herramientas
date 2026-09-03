import os
from modulos.prestamos import prestamos, cargar_herramientas

def ver_mi_historial(usuario_actual):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------------------")
    print(f"   MIS SOLICITUDES Y PRÉSTAMOS - [{usuario_actual['nombre']}]")
    print("-----------------------------------------")
    
    # Filtrar préstamos del usuario actual
    mis_prestamos = [p for p in prestamos if str(p["usuario_id"]) == str(usuario_actual["id"])]
    
    if not mis_prestamos:
        print("No tienes solicitudes o préstamos registrados.")
        input("\nPresione Enter para volver...")
        return

    herramientas = cargar_herramientas()
    
    # Función auxiliar para obtener el nombre de la herramienta
    def obtener_nombre_herramienta(h_id):
        for h in herramientas:
            if h.get("id") == h_id:
                return h.get("nombre", "Desconocida")
        return "Desconocida"

    print(f"{'ID':<10} | {'Herramienta':<15} | {'Cant':<5} | {'Estado':<10} | {'Fecha Inicio'}")
    print("-" * 70)
    
    for p in mis_prestamos:
        nombre_h = obtener_nombre_herramienta(p["herramienta_id"])
        print(f"{p['id_prestamo']:<10} | {nombre_h:<15} | {p['cantidad']:<5} | {p['estado']:<10} | {p['fecha_inicio']}")
    
    input("\nPresione Enter para continuar...")
