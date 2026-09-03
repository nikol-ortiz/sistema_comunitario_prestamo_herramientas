import os, logging
from modulos.functions import cargar_json_lista

ruta = "data/usuarios.json"
os.makedirs("data", exist_ok=True)

def cargar_usuarios():
    return cargar_json_lista(ruta)

def iniciar_sesion():
    print('--- INICIO DE SESIÓN ---')
    username = input('Ingrese su ID para iniciar sesión: ').strip()
    usuarios = cargar_usuarios()
    
    # Buscamos si existe el usuario
    for usuario in usuarios:
        if usuario['id'] == username:
            print(f"\n¡Bienvenido/a, {usuario['nombre']}!")
            logging.info(f"Usuario {usuario['nombre']} ({usuario['id']}) inició sesión.")
            input("Presione Enter para continuar...")
            return usuario  # Retorna el diccionario completo del usuario
            
    # Si termina el ciclo for y no lo encuentra:
    print('\nUsuario no encontrado...')
    logging.warning(f"Intento fallido de inicio de sesión con ID: {username}")
    input("Presione Enter para continuar...")
    return None