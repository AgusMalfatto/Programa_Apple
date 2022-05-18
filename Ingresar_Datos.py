import string

def Generar_ID(lista_id):
    nuevo_id = lista_id[-1] + 1
    lista_id.append(nuevo_id)
    return nuevo_id

def Ingresar_Opcion_Menu(mensaje, mensaje_error, min, max):
    valido = 1
    while valido == 1:
        try:
            num = input(mensaje)
            assert int(num) >= min and int(num) <= max
            valido = 0
        except:
            print(mensaje_error)
    return int(num)

def Ingresar_Descripcion(mensaje):
    valido = 1
    while valido == 1:
        try:
            descripcion = input(mensaje)
            for letra in descripcion:
                assert not(letra in string.punctuation)
            valido = 0
        except:
            print("Descripción no válida.")
    return descripcion

def Ingresar_Nacionalidad(mensaje):
    valido = 1
    nacionalidades = ('CHINA', 'EEUU', 'ESPAÑA')
    while valido == 1:
        try:
            nacionalidad = input(mensaje)
            nuevo = nacionalidad.upper()
            valor = nuevo in nacionalidades
            assert valor
            valido = 0
        except:
            print("Nacionalidad no válida.")
    return nacionalidad.upper()

def Ingresar_Tipo(mensaje):
    valido = 1
    tipos_validos = ('IPHONE', 'TABLET', 'MAC', 'SMART WATCH')
    while valido == 1:
        try:
            tipo = input(mensaje)
            assert tipo.upper() in tipos_validos
            valido = 0
        except:
            print("Tipo de producto no válido.")
    return tipo.upper()

def Ingresar_Precio(mensaje):
    valido = 1
    while valido == 1:
        try:
            precio = input(mensaje)
            for i in precio:
                assert i in string.digits
            assert int(precio) >= 1000 and int(precio) <= 10000
            valido = 0
        except:
            print("Precio de producto no válido.")
    return int(precio)
   
def Ingresar_un_Producto(lista, lista_id):
    id_producto = Generar_ID(lista_id)
    descripcion = Ingresar_Descripcion("Ingrese la descripción: ")
    nacionalidad = Ingresar_Nacionalidad("Ingrese la nacionalidad (China, EEUU o España): ")
    tipo = Ingresar_Tipo("Ingrese el tipo (Iphone, Tablet, Mac o Smart watch): ")
    precio = Ingresar_Precio("Ingrese el precio (Entre 1000 y 10000): ")
    '''
    producto = {
        "id_producto" : 0,
        "descripcion" : "",
        "nacionalidad" : "",
        "tipo" : "",
        "precio" : 0
    }'''
    producto = dict()
    producto["id_producto"] = id_producto
    producto["descripcion"] = descripcion
    producto["nacionalidad"] = nacionalidad
    producto["tipo"] = tipo
    producto["precio"] = precio
    
    lista.append(producto)
    
def Mostrar_un_Producto(producto):
    print("{:<11} | {:<15} | {:<12} | {:<15} | {:<11} |".format(producto['id_producto'], producto['descripcion'], producto['nacionalidad'], producto['tipo'], producto['precio']))

def Mostrar_Productos(lista):
    print("\n\n{:<10} | {:<15} | {:<10} | {:<15} | {:<11} |\n".format('Id producto', 'Descripcion', 'Nacionalidad', 'Producto', 'Precio'))
    for producto in lista:
        Mostrar_un_Producto(producto)