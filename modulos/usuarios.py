
# Operaciones: crear, listar, buscar, actualizar y eliminar usuarios.
import os,json
from modulos.functions import leer_entero, cargar_json_lista

# Esta es la ruta del JSON de las usuarios
ruta = "data/usuarios.json"
os.makedirs("data", exist_ok=True)

usuarios = cargar_json_lista(ruta)
            



#mostrar menu de gestion de usuarios
def mostrar_menu_gestion_usuarios():
    opcion_gestion_usuarios = 0
    while opcion_gestion_usuarios != 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------")
        print("----Gestion de usuarios------")
        print("-----------------------------")
        print("1. Agregar usuario")
        print("2. Eliminar usuario")
        print("3. Modificar usuario")
        print("4. Consultar usuario")
        print("5. Listar usuarios")
        print("6. Volver al menu principal")
        opcion_gestion_usuarios = leer_entero("Seleccione una opción: ")

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
    print("----Crear usuario------")
    print("-----------------------------")
    identidad = input("Ingrese la identidad del usuario: ")
    nombre = input("Ingrese el nombre del usuario: ")
    apellido = input("Ingrese el apellido del usuario: ")
    telefono = input("Ingrese el telefono del usuario: ")
    direccion = input("Ingrese la direccion del usuario: ")
    administrador = leer_entero("Ingrese si el usuario es administrador (1: USUARIO       2: ADMINISTRADOR): ")
    if administrador == 2:
        administrador = True
    else:
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
    print("----Eliminar usuario------")
    print("-----------------------------")
    quiere_listar = leer_entero("¿Quiere listar los usuarios (1: Si, 2: No)? ")
    if quiere_listar == 1:
        listar_usuarios()
        
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
    print("----Modificar usuario------")
    print("-----------------------------")
    quiere_listar = leer_entero("¿Quiere listar los usuarios (1: Si, 2: No)? ")
    if quiere_listar == 1:
        listar_usuarios()
    usuario_id = input("Ingrese la identidad del usuario a modificar: ")
    
    # Buscar el usuario por identidad
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            print('Datos del usuario:')
            print(f'Id: {usuario["id"]} \n Nombre: {usuario["nombre"]} \n Apellido: {usuario["apellido"]} \n Telefono: {usuario["telefono"]} \n Direccion: {usuario["direccion"]} \n Tipo de usuario: {"Administrador" if usuario["tipo_de_usuario"] else "Usuario"}')
            print('Qué quieres modificar?')
            opcion = leer_entero("1. Nombre \n2. Apellido \n3. Telefono \n4. Direccion \n5. Tipo de usuario \nIngrese tu elección: ")
            if opcion == 1:
                nombre = input("Ingrese el nuevo nombre del usuario: ")
                usuario["nombre"] = nombre
            elif opcion == 2:
                apellido = input("Ingrese el nuevo apellido del usuario: ")
                usuario["apellido"] = apellido
            elif opcion == 3:
                telefono = input("Ingrese el nuevo telefono del usuario: ")
                usuario["telefono"] = telefono
            elif opcion == 4:
                direccion = input("Ingrese la nueva direccion del usuario: ")
                usuario["direccion"] = direccion
            elif opcion == 5:
                administrador = leer_entero("Ingrese si el usuario es administrador (1: USUARIO       2: ADMINISTRADOR): ")
                if administrador == 2:
                    administrador = True
                else:
                    administrador = False
                usuario["tipo_de_usuario"] = administrador
            elif opcion == 6:
                volver_menu_principal()
            else:
                print("Opción invalida")
                return
            
            # Guardar la lista de usuarios en el archivo JSON
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            
            print("Usuario modificado exitosamente.")
            input("Presione Enter para continuar...")
            return
    
    print("Usuario no encontrado.")
    input("Presione Enter para continuar...")

#4 Consultar usuario
def consultar_usuario():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("----Consultar usuario------")
    print("-----------------------------")
    usuario_id = input("Ingrese la identidad del usuario a consultar: ")
    
    # Buscar el usuario por identidad
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            print("Usuario encontrado:")
            print(f"Identidad: {usuario['id']}")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Apellido: {usuario['apellido']}")
            print(f"Telefono: {usuario['telefono']}")
            print(f"Direccion: {usuario['direccion']}")
            print(f"Tipo de usuario: {'Administrador' if usuario['tipo_de_usuario'] else 'Usuario'}")
            input("Presione Enter para continuar...")
            return
    
    print("Usuario no encontrado.")
    input("Presione Enter para continuar...")

#5 Listar usuarios
def listar_usuarios():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("----Listar usuarios------")
    print("-----------------------------")
    
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    
    for usuario in usuarios:
        print(f"Identidad: {usuario['id']}")
        print(f"Nombre: {usuario['nombre']}")
        print(f"Apellido: {usuario['apellido']}")
        print(f"Telefono: {usuario['telefono']}")
        print(f"Direccion: {usuario['direccion']}")
        print(f"Tipo de usuario: {'Administrador' if usuario['tipo_de_usuario'] else 'Usuario'}")
        print("-----------------------------")
    input("Presione Enter para continuar...")

#6 Volver al menu principal
def volver_menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("----Volver al menu principal------")
    print("-----------------------------")
    input("Presione Enter para continuar")

