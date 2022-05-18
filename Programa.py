'''Una empresa importadora que comercializa productos Apple, decide registrar de sus productos los siguientes datos:
idProducto (numerico)
descripcion (alfanumérico)
nacionalidad (EEUU - CHINA - OTRO)
tipo (IPHONE -MAC - IPAD - ACCESORIOS)
precio (numérico decimal)
Realizar un programa que permita interactuar con un menú de usuarios con las siguientes opciones:
ALTA Producto: Se ingresan los datos de UN solo producto. Siempre y cuando haya espacio disponible en el array.
BAJA Producto: A partir del ingreso del ID. Si existe el producto desaparece de la lista, dejando espacio disponible para un nuevo producto.
MODIFICACIÓN Producto: A partir del ingreso del ID. Si existe se podrá modificar el precio o el tipo.
LISTADO Productos.
LISTADO ordenado por precio.
LISTADO ordenado por descripción.
El/los  productos más caros.
Precio promedio por tipo de producto.
De los Iphone el más barato
 ============================================================================
Ejercicio 10-3:
Agregar la estructura etipoProducto, que definirá los siguientes campos:
idTipo (numérico)
descripcionTipo(alfanumérico)
Para esta estructura en principio trabajaremos con datos hardcodeados:


-El listado de todos los productos con la descripción del tipo.
-Por cada tipo la lista de productos.

Ejercicio 11.1:
El/los tipos de productos con mas productos importados.

Ejercicio 12:
La nacionalidad que solo fabrica Iphone.
Los productos, ordenados por nacionalidad alfabéticamente.
La nacionalidad con más tipos de productos fabricados.
El precio promedio de productos por nacionalidad
'''
 
from Operaciones import *

lista_id = [99, 100, 101, 102, 103, 104, 105]
lista_Productos = [
    {"id_producto" : 100,
        "descripcion" : "PI0042521A",
        "nacionalidad" : "EEUU",
        "tipo" : "IPHONE",
        "precio" : 5500},
    {"id_producto" : 101,
        "descripcion" : "PI0042588G",
        "nacionalidad" : "CHINA",
        "tipo" : "MAC",
        "precio" : 6800},
    {"id_producto" : 102,
        "descripcion" : "PI0041215D",
        "nacionalidad" : "EEUU",
        "tipo" : "TABLET",
        "precio" : 3600},
    {"id_producto" : 103,
        "descripcion" : "PI0043233C",
        "nacionalidad" : "CHINA",
        "tipo" : "IPHONE",
        "precio" : 3100},
    {"id_producto" : 104,
        "descripcion" : "PI0045658H",
        "nacionalidad" : "EEUU",
        "tipo" : "MAC",
        "precio" : 4600},
    {"id_producto" : 105,
        "descripcion" : "PI0041414S",
        "nacionalidad" : "ESPAÑA",
        "tipo" : "SMART WATCH",
        "precio" : 2300}
]

opcion = 0

while opcion != 8:
    print('\n******** MEN OPCIONES ********\n')
    print('1. Ingresar nuevo producto.')
    print('2. Dar de baja un producto.')
    print('3. Modifica un producto.')
    print('4. Listar productos en Stock.')
    print('5. Listar productos en Stock por precio.')
    print('6. Filtrar productos.')
    print('7. Precio promedio por productos.')
    print('8. CERRAR PROGRAMA')
    
    opcion = Ingresar_Opcion_Menu('\nIngrese la opcion: ', '\nOpción de menú no válida.\n', 1, 9)
    
    if opcion ==  1:
        Ingresar_un_Producto(lista_Productos, lista_id)
    if opcion ==  2:
        lista_Productos = Dar_de_Baja(lista_Productos)
    elif opcion ==  3:
        Modificar_Producto(lista_Productos)
    elif opcion ==  4:
        Mostrar_Productos(lista_Productos)
    elif opcion ==  5:
        Listar_Por_Precio(lista_Productos)
    elif opcion ==  6:
        Menu_Filtros(lista_Productos)
    elif opcion ==  7:
        Promedio(lista_Productos)

print(lista_Productos)