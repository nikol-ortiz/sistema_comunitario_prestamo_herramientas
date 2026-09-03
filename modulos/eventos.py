import os
import logging

# Crear carpeta data y configurar logging global
os.makedirs("data", exist_ok=True)

logging.basicConfig(
    filename="data/app.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

# Asi se puede usar:
# # Usas las funciones directamente
# logging.info("Sistema iniciado correctamente.")
# logging.warning("Intento de eliminar herramienta con ID inexistente.")
# logging.error("Error al guardar los datos en el JSON.")


def ver_registro_eventos():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------------")
        print("--- REGISTRO DE EVENTOS (LOGS) ---")
        print("-----------------------------------")
        print("1. Ver todos los eventos")
        print("2. Ver información (INFO)")
        print("3. Ver alertas (WARNING)")
        print("4. Ver errores (ERROR)")
        print("5. Volver al menú principal")
        print("-----------------------------------")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '5':
            break
            
        if opcion not in ['1', '2', '3', '4']:
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue

        try:
            with open("data/app.log", "r", encoding="utf-8") as file:
                logs = file.readlines()
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"--- MOSTRANDO EVENTOS ---")
            
            filtro = ""
            if opcion == '2': filtro = "[INFO]"
            elif opcion == '3': filtro = "[WARNING]"
            elif opcion == '4': filtro = "[ERROR]"
            
            encontrado = False
            for line in logs:
                if filtro in line:
                    print(line.strip())
                    encontrado = True
            
            if not encontrado:
                print(f"\nNo se encontraron eventos con el filtro: {filtro if filtro else 'Todos'}")
                
        except FileNotFoundError:
            print("Error: El archivo de registros 'data/app.log' no existe.")
        except Exception as e:
            print(f"Error al leer los registros: {e}")
            
        input("\nPresione Enter para volver al menú de eventos...")

    logging.info("Salió de la visualización de eventos")
    return