import json

# Inicialización de matrices para almacenar nombres de usuario y contraseñas
usuarios = [''] * 8
contraseñas = [[''] * 8 for _ in range(8)]

# Diccionario para almacenar los datos de usuarios
datos_usuarios = {}

# Función para crear un nuevo usuario
def crear_usuario():
    global datos_usuarios
    if len(datos_usuarios) < 8:
        nuevo_usuario = input("Ingrese el nombre de usuario: ")
        nueva_contraseña = input("Ingrese una contraseña de 8 caracteres: ")
        pregunta1 = input("Ingrese una pregunta de seguridad (fácil de recordar): ")
        respuesta1 = input("Ingrese la respuesta a la pregunta de seguridad: ")
        pregunta2 = input("Ingrese otra pregunta de seguridad (diferente a la anterior): ")
        respuesta2 = input("Ingrese la respuesta a la segunda pregunta de seguridad: ")
        
        # Verificar la longitud de la contraseña
        if len(nueva_contraseña) == 8:
            datos_usuarios[nuevo_usuario] = {
                'contraseña': nueva_contraseña,
                'pregunta1': pregunta1,
                'respuesta1': respuesta1,
                'pregunta2': pregunta2,
                'respuesta2': respuesta2
            }
            guardar_datos_usuarios()
            print("Usuario creado exitosamente!")
            print("Datos de usuario:", datos_usuarios)  # Mensaje de depuración
        else:
            print("La contraseña debe tener exactamente 8 caracteres.")
    else:
        print("Ya se han creado el máximo número de usuarios.")

# Función para guardar los datos de usuarios en un archivo JSON
def guardar_datos_usuarios():
    with open('datos_usuarios.json', 'w') as f:
        json.dump(datos_usuarios, f)

# Función para cargar los datos de usuarios desde un archivo JSON
def cargar_datos_usuarios():
    global datos_usuarios
    try:
        with open('datos_usuarios.json', 'r') as f:
            datos_usuarios = json.load(f)
    except FileNotFoundError:
        pass

# Función para el proceso de inicio de sesión
def login():
    global datos_usuarios
    # Solicitar al usuario que ingrese su nombre de usuario
    input_usuario = input("Ingrese su nombre de usuario: ")
    print("Usuarios registrados:", datos_usuarios.keys())  # Mensaje de depuración
    
    # Verificar si el usuario existe
    if input_usuario in datos_usuarios:
        input_contraseña = input("Ingrese su contraseña: ")
        
        # Verificar si la contraseña coincide
        if input_contraseña == datos_usuarios[input_usuario]['contraseña']:
            print("Inicio de sesión exitoso!")
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario no encontrado.")

# Función para restablecer la contraseña
def restablecer_contraseña():
    global datos_usuarios
    usuario = input("Ingrese su nombre de usuario: ")
    if usuario in datos_usuarios:
        respuesta1 = input(datos_usuarios[usuario]['pregunta1'] + ": ")
        respuesta2 = input(datos_usuarios[usuario]['pregunta2'] + ": ")
        if respuesta1 == datos_usuarios[usuario]['respuesta1'] and respuesta2 == datos_usuarios[usuario]['respuesta2']:
            nueva_contraseña = input("Ingrese una nueva contraseña de 8 caracteres: ")
            if len(nueva_contraseña) == 8:
                datos_usuarios[usuario]['contraseña'] = nueva_contraseña
                guardar_datos_usuarios()
                print("Contraseña restablecida exitosamente.")
            else:
                print("La contraseña debe tener exactamente 8 caracteres.")
        else:
            print("Respuestas incorrectas.")
    else:
        print("Usuario no encontrado.")

# Función para mostrar algoritmos de ordenamiento
def mostrar_algoritmos_ordenamiento():
    print("Los algoritmos de ordenamiento disponibles son:")
    # Aquí puedes incluir tu implementación de algoritmos de ordenamiento o simplemente describirlos

# Función para mostrar estructuras de árbol
def mostrar_estructuras_arbol():
    print("Las estructuras de árbol disponibles son:")
    # Aquí puedes incluir tu implementación de estructuras de árbol o simplemente describirlas

# Función principal para mostrar el menú de opciones
def menu():
    cargar_datos_usuarios()
    while True:
        print("\nMenú de opciones:")
        print("1. Iniciar sesión")
        print("2. Crear usuario")
        print("3. Restablecer contraseña")
        print("4. Ver algoritmos de ordenamiento")
        print("5. Ver estructuras de árbol")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            login()
        elif opcion == '2':
            crear_usuario()
        elif opcion == '3':
            restablecer_contraseña()
        elif opcion == '4':
            mostrar_algoritmos_ordenamiento()
        elif opcion == '5':
            mostrar_estructuras_arbol()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

# Ejecutar el programa
menu()

