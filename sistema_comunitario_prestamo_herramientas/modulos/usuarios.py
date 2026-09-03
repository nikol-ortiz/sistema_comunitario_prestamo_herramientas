
# Operaciones: crear, listar, buscar, actualizar y eliminar usuarios.
import os,json
ruta_archivo = 'data/usuarios.json'

# Crear la carpeta data si no existe
os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

if not os.path.exists(ruta_archivo):
    with open(ruta_archivo, 'w') as f:
        json.dump([], f)
# Esta es la ruta del JSON de las usuarios
ruta = "data/usuarios.json"
os.makedirs("data", exist_ok=True)

if os.path.exists("data"):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            usuarios = json.load(f)
    except json.decoder.JSONDecodeError:
        usuarios=[]
else:
    usuarios=[]
            



#mostrar menu de gestion de usuarios
def mostrar_menu_gestion_usuarios():
    opcion_gestion_usuarios = 0
    while opcion_gestion_usuarios != 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------")
        print("gestion de usuarios")
        print("-----------------------------")
        print("1. agregar usuario")
        print("2. eliminar usuario")
        print("3. modificar usuario")
        print("4. consultar usuario")
        print("5. listar usuarios")
        print("6. Volver al menu principal")
        opcion_gestion_usuarios = int(input("Seleccione una opción: "))

        if opcion_gestion_usuarios == 1:
            print('Agregar usuario')
            crear_usuario()
        elif opcion_gestion_usuarios == 2:
            print('Eliminar usuario')
            eliminar_usuario()
        elif opcion_gestion_usuarios == 3:
            print('Modificar usuario')
            modificar_usuario()
        elif opcion_gestion_usuarios == 4:
            print('Consultar usuario')
            consultar_usuario()
        elif opcion_gestion_usuarios == 5:
            print('Listar usuarios')
            listar_usuarios()
        elif opcion_gestion_usuarios == 6:
            print("Volver al menu principal")
            volver_menu_principal()
        else:
            print("Opción invalida")

#1 crear usuario
def crear_usuario():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("crear usuario")
    print("-----------------------------")
    identidad = input("Ingrese la identidad del usuario: ")
    nombre = input("Ingrese el nombre del usuario: ")
    apellido = input("Ingrese el apellido del usuario: ")
    telefono = input("Ingrese el telefono del usuario: ")
    direccion = input("Ingrese la direccion del usuario: ")
    administrador = int(input("Ingrese si el usuario es administrador (1: USUARIO       2: ADMINISTRADOR): "))
    if administrador == 2:
        administrador = True
        print(" administrador.")
    else:
        print("usuario")
        administrador = False

    # Crear un diccionario con los datos del usuario
    usuario = {
        "id": identidad,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "direccion": direccion,
        "tipo_de_usuario": administrador 
    }
    
    # Agregar el usuario a la lista de usuarios
    usuarios.append(usuario)
    
    # Guardar la lista de usuarios en el archivo JSON
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)
    
    print("Usuario creado exitosamente.")
    
#2 Eliminar usuario
def eliminar_usuario():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("eliminar usuario")
    print("-----------------------------")
    usuario_id = input("Ingrese la identidad del usuario a eliminar: ")

    # Buscar el usuario por identidad
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            usuarios.remove(usuario)  # Corregido: se remueve el diccionario completo
            
            # Guardar la lista de usuarios en el archivo JSON
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            
            print("Usuario eliminado exitosamente.")
            input("Presione Enter para continuar...")
            return
    
    # Corregido: fuera del for, se ejecuta solo si recorrió toda la lista y no encontró coincidencia
    print("Usuario no encontrado")
    input("Presione Enter para continuar..")

#3 Modificar usuario"Presione Enter para continuar..."
def modificar_usuario():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("modificar usuario")
    print("-----------------------------")
    usuario_id = input("Ingrese la identidad del usuario a modificar: ")
    
    # Buscar el usuario por identidad
    for usuario in usuarios:
        if usuario.get("usuario_id") == usuario_id or usuario.get("id") == usuario_id:
            nombre = input("Ingrese el nuevo nombre del usuario: ")
            apellido = input("Ingrese el nuevo apellido del usuario: ")
            telefono = input("Ingrese el nuevo telefono del usuario: ")
            direccion = input("Ingrese la nueva direccion del usuario: ")
            administrador = int(input("Ingrese si el usuario es administrador (1: USUARIO       2: ADMINISTRADOR): "))
            if administrador == 2:
                administrador = True
                print(" administrador.")
            else:
                administrador = False
                print("usuario")
            
            # Actualizar los datos del usuario
            usuario["nombre"] = nombre
            usuario["apellido"] = apellido
            usuario["telefono"] = telefono
            usuario["direccion"] = direccion
            usuario["tipo_de_usuario"] = administrador
            
            # Guardar la lista de usuarios en el archivo JSON
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            
            print("Usuario modificado exitosamente.")
            return
    
    print("Usuario no encontrado.")

#4 Consultar usuario
def consultar_usuario():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("consultar usuario")
    print("-----------------------------")
    usuario_id = input("Ingrese la identidad del usuario a consultar: ")
    
    # Buscar el usuario por identidad
    for usuario in usuarios:
        if usuario.get("id") == usuario_id:
            print("Usuario encontrado:")
            print(f"Identidad: {usuario['usuario_id']}")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Apellido: {usuario['apellido']}")
            print(f"Telefono: {usuario['telefono']}")
            print(f"Direccion: {usuario['direccion']}")
            print(f"Tipo de usuario: {'Administrador' if usuario['tipo_de_usuario'] else 'Usuario'}")
            return
    
    print("Usuario no encontrado.")

#5 Listar usuarios

def listar_usuarios():
    # 1. Cargar la lista actualizada desde el archivo JSON
    try:
        with open('data/usuarios.json', 'r') as archivo:
            usuarios = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        usuarios = []

    # 2. Verificar si está vacía
    if not usuarios:
        print("No hay usuarios registrados.")
        input("\nPresione Enter para continuar...")
        return

    # 3. Mostrar la lista
    for usuario in usuarios:
        print(f"Identidad: {usuario.get('usuario_id', usuario.get('id', 'N/A'))}")
        print(f"Nombre: {usuario.get('nombre', 'N/A')}")
        print(f"Apellido: {usuario.get('apellido', 'N/A')}")
        print(f"Telefono: {usuario.get('telefono', 'N/A')}")
        print(f"Direccion: {usuario.get('direccion', 'N/A')}")
        
        tipo = 'Administrador' if usuario.get('tipo_de_usuario') else 'Usuario'
        print(f"Tipo de usuario: {tipo}")
        print("------------------------------")
    
    input("\nPresione Enter para continuar...")
#6 Volver al menu principal
def volver_menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("volver al menu principal")
    print("-----------------------------")
    input("Presione Enter para continuar")
