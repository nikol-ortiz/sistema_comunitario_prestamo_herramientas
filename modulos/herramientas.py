import os, json

# Ruta del JSON
ruta = "data/herramientas.json"

# Asegura que la carpeta data exista
os.makedirs("data", exist_ok=True)

# Cargar datos existentes o inicializar lista vacía
if os.path.exists(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            herramientas = json.load(f)
    except json.JSONDecodeError:
        herramientas = []
else:
    herramientas = []

# Funcion para limpiar pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menú principal de la gestión de herramientas
def mostrar_menu_gestion_herramientas():
    opcion_gestion_herramientas = 0
    while opcion_gestion_herramientas != 6:
        limpiar_pantalla()
        print("-----------------------------")
        print("Gestión de herramientas")
        print("-----------------------------")
        print("1. Agregar herramienta")
        print("2. Eliminar herramienta")
        print("3. Modificar herramienta")
        print("4. Buscar herramienta")
        print("5. Listar herramientas")
        print("6. Volver al menú principal")
        
        try:
            opcion_gestion_herramientas = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            input("Presione Enter para continuar...")
            continue

        if opcion_gestion_herramientas == 1:
            agregar_herramienta()
        elif opcion_gestion_herramientas == 2:
            eliminar_herramientas()
        elif opcion_gestion_herramientas == 3:
            modificar_herramientas()
        elif opcion_gestion_herramientas == 4:
            buscar_herramienta()
        elif opcion_gestion_herramientas == 5:
            listar_herramientas()
        elif opcion_gestion_herramientas == 6:
            print("Volver al menú principal")
        else:
            print("Opción inválida, por favor intente de nuevo.")
            input("Presione Enter para continuar...")

# Función para agregar una herramienta
def agregar_herramienta():
    limpiar_pantalla()
    print('--- Agregar herramienta ---')
    id = int(input("Ingrese el ID de la herramienta: "))
    nombre = input("Ingrese el nombre de la herramienta: ")
    categoria = input("Ingrese la categoría de la herramienta: ")
    cantidad_disponible = int(input("Ingrese la cantidad disponible: "))

    print('Ingrese el estado de la herramienta:')
    print('1. Activa')
    print('2. En reparación')
    print('3. Fuera de servicio')
    estado = int(input("Seleccione una opción: "))
    if estado not in [1, 2, 3]:
        print("Opción inválida, por favor intente de nuevo.")
        input("Presione Enter para continuar...")
        return
    
    valor_estimado = float(input("Ingrese el valor estimado de la herramienta: "))

    # Agrega la herramienta a la lista en memoria
    herramientas.append({
        "id": id,
        "nombre": nombre.upper().strip(),
        "categoria": categoria.upper().strip(),
        "cantidad_disponible": cantidad_disponible,
        "estado": estado,
        "valor_estimado": valor_estimado
    })

    #Aqui hacemos el guardado en archivo JSON
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(herramientas, f, ensure_ascii=False, indent=4)

    print("Herramienta agregada con éxito.")
    input("Presione Enter para continuar...")

# Función para listar una herramientas
def listar_herramientas():
    limpiar_pantalla()
    print('--- Listar herramientas ---')
    if not herramientas:
        print("No hay herramientas registradas.")
    else:
        for herramienta in herramientas:
            print(f"ID: {herramienta['id']}, Nombre: {herramienta['nombre']}, Categoría: {herramienta['categoria']}, Cantidad disponible: {herramienta['cantidad_disponible']}, Estado: {herramienta['estado']}, Valor estimado: {herramienta['valor_estimado']}")
    input("Presione Enter para continuar...")

# Función para Eliminar una herramienta
def eliminar_herramientas():
    limpiar_pantalla()
    print('--- Eliminar herramienta ---')
    opcion_eliminar_herramientas = 0
    opcion_eliminar_herramientas = int(input('Quieres listar las herramientas?    1> SI   2> No         '))
    if opcion_eliminar_herramientas == 1:
        listar_herramientas()

    id_herraminta_eliminar = int(input("Ingrese el ID de la herramienta a eliminar: "))
    encontrado = False
    for herramienta in herramientas:
        if herramienta['id'] == id_herraminta_eliminar:
            encontrado = True
            herramientas.remove(herramienta)
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(herramientas, f, ensure_ascii=False, indent=4)
            print("Herramienta eliminada con éxito.")
            input("Presione Enter para continuar...")
            break
    if not encontrado:
        print("Herramienta no encontrada.")
        input("Presione Enter para continuar...")
        return

# Función para Modificar una herramienta
def modificar_herramientas():
    limpiar_pantalla()
    print('--- Modificar herramienta ---')
    opcion_modificar_herramientas = 0
    opcion_modificar_herramientas = int(input('Quieres listar las herramientas?    1> SI   2> No         '))
    if opcion_modificar_herramientas == 1:
        listar_herramientas()

    id_herramienta_modificar = int(input("Ingrese el ID de la herramienta a modificar: "))
    encontrada = False
    for herramienta in herramientas:
        if herramienta['id'] == id_herramienta_modificar:
            encontrada = True
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"ID: {herramienta['id']}, Nombre: {herramienta['nombre']}, Categoría: {herramienta['categoria']}, Cantidad disponible: {herramienta['cantidad_disponible']}, Estado: {herramienta['estado']}, Valor estimado: {herramienta['valor_estimado']}")
            print('Qué quieres modificar?')
            print('1. Nombre')
            print('2. Categoría')
            print('3. Cantidad disponible')
            print('4. Estado')
            print('5. Valor estimado')
            opcion_modificar = int(input("Seleccione una opción: "))

            actualizacion = None
            parametro = None

            if opcion_modificar == 1:
                nombre = input("Ingrese el nuevo nombre de la herramienta: ")
                actualizacion = nombre.upper().strip()
                parametro = 'nombre'
                input("Presione Enter para continuar...")
                
            elif opcion_modificar == 2:
                categoria = input("Ingrese la nueva categoria de la herramienta: ")
                actualizacion = categoria.upper().strip()
                parametro = 'categoria'
                input("Presione Enter para continuar...")
                
            elif opcion_modificar == 3:
                cantidad = int(input("Ingrese la nueva cantidad de la herramienta: "))
                actualizacion = cantidad
                parametro = 'cantidad_disponible'
                input("Presione Enter para continuar...")

            elif opcion_modificar == 4:
                print('Ingrese el nuevo estado de la herramienta: ')
                print('1. Activa')
                print('2. En reparación')
                print('3. Fuera de servicio') 
                estado = int(input("Seleccione una opción: "))
                if estado not in [1, 2, 3]:
                    print("Opción inválida, por favor intente de nuevo.")
                    input("Presione Enter para continuar...")
                    return
                actualizacion = estado
                parametro = 'estado'
                input("Presione Enter para continuar...")
                
            elif opcion_modificar == 5:
                valor = int(input("Ingrese el nuevo valor de la herramienta: "))
                actualizacion = valor
                parametro = 'valor_estimado'
                input("Presione Enter para continuar...")
                
            else:
                print('Opcion no disponible')
                return

            # Aqui se hace la actualizacion en el archivo json
            if parametro and actualizacion is not None:
                herramienta[parametro] = actualizacion
                with open(ruta, "w", encoding="utf-8") as f:
                    json.dump(herramientas, f, ensure_ascii=False, indent=4)
                print("Modificado con éxito.")
                input("Presione Enter para continuar...")
            
            break # Salir del bucle for ya que encontramos la herramienta

    if not encontrada:
        print("Herramienta no encontrada.")
        input("Presione Enter para continuar...")

# Función para Buscar una herramienta
def buscar_herramienta():
    limpiar_pantalla()
    print('--- Buscar herramienta ---')
    try:
        id_herramienta_buscar = int(input("Ingrese el ID de la herramienta a buscar: "))
    except ValueError:
        print("El ID debe ser un número entero válido.")
        input("Presione Enter para continuar...")
        return

    encontrado = False
    
    # Mapeo numérico de estados a texto
    estados = {
        1: "Activa/Disponible",
        2: "En reparación",
        3: "Fuera de servicio"
    }

    for herramienta in herramientas:
        if herramienta['id'] == id_herramienta_buscar:
            encontrado = True
            print("\n¡Herramienta encontrada!")
            estado_texto = estados.get(herramienta['estado'], "Desconocido")
            
            print(f"ID: {herramienta['id']} | "
                  f"Nombre: {herramienta['nombre']} | "
                  f"Categoría: {herramienta['categoria']} | "
                  f"Unidades disponibles: {herramienta['cantidad_disponible']} | "
                  f"Estado: {estado_texto} | "
                  f"Valor estimado: ${herramienta['valor_estimado']:,.2f}")
            input("\nPresione Enter para continuar...")
            break

    if encontrado == False: 
        print(f"\nNinguna herramienta coincide con el ID: {id_herramienta_buscar}")
        try:
            continuar = int(input('¿Quieres buscar otro ID? 1: SI | 2: NO: '))
            if continuar == 1:
                buscar_herramienta()
        except ValueError:
            pass
    