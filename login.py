import json, os, logging

ruta = "data/usuarios.json"
os.makedirs("data", exist_ok=True)

def cargar_usuarios():
    if os.path.exists(ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.decoder.JSONDecodeError:
            return []
    return []

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