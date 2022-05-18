from Ingresar_Datos import *

def Menu_Modificar(lista, indice):
    opcion = 0
    while opcion != 4:
        print("1. Modificar descripción")
        print("2. Modificar nacionalidad")
        print("3. Modificar precio")
        print("4. Volver al menú principal")

        opcion = Ingresar_Opcion_Menu("Ingrese la opción del detalle a modificar: ", "Opción menú fuera de rango", 1, 4)

        if opcion == 1:
            nueva_descripcion = Ingresar_Descripcion("Ingrese la nueva descripción: ")
            lista[indice]["descripcion"] = nueva_descripcion # Reemplazo la nueva descripción
        elif opcion == 2:
            nueva_nacionalidad = Ingresar_Nacionalidad("Ingrese la nueva nacionalidad: ")
            lista[indice]["nacionalidad"] = nueva_nacionalidad # Reemplazo la nueva nacionalidad
        elif opcion == 3:
            nuevo_precio = Ingresar_Precio("Ingrese el nuevo precio: ")
            lista[indice]["precio"] = nuevo_precio # Reemplazo por el nuevo precio

def Dar_de_Baja(lista):
    Mostrar_Productos(lista)
    id_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
    # Recorro los productos
    for i in range(len(lista)):
        producto = lista[i]
        # Si el id que se desea eliminar es el del producto encontrado
        if producto["id_producto"] == id_eliminar:
            del lista[i]
            break
    return lista
    
def Modificar_Producto(lista):
    Mostrar_Productos(lista)
    id_modificar = int(input("Ingrese el ID del producto que desee modificar: "))
    # Recorro los productos
    for i in range(len(lista)):
        producto = lista[i]
        # Si el id del producto a modificar es el encontrado
        if producto["id_producto"] == id_modificar:
            Mostrar_un_Producto(producto)
            Menu_Modificar(lista, i)

def Listar_Por_Precio(lista):
    valor = 1
    while valor == 1:
        try:
            precio_minimo = Ingresar_Opcion_Menu("Ingrese el precio mínimo: ", "Precio fuera de rango", 0, 10000)
            precio_maximo = Ingresar_Opcion_Menu("Ingrese el precio máximo: ", "Precio fuera de rango", 0, 10000)
            assert precio_minimo <= precio_maximo
            valor = 0
        except:
            print("El precio mínimo debe ser menor al precio máximo.")

    nueva_lista = [] # Lista para los productos con el precio dentro del rango ingresado

    # Recorro la lista de productos
    for producto in lista:
        # Si el precio del producto se encuentra en el rango ingresado
        if (producto["precio"] >= precio_minimo) and (producto["precio"] <= precio_maximo):
            if len(nueva_lista) == 0:
                nueva_lista.append(producto)
            else:
                # Recorro los productos con el rango
                for i in range(len(nueva_lista)):
                    # Si el precio es mayor lo coloco antes
                    if nueva_lista[i]["precio"] < producto["precio"]:
                        nueva_lista.insert(i, producto)
                        break
                    if i == len(nueva_lista) - 1:
                        nueva_lista.append(producto)
    Mostrar_Productos(nueva_lista)

def Filtrar(lista, filtro, codigo):
    nueva_lista = []
    if codigo == 1:
        cadena = Ingresar_Nacionalidad("\nIngrese la nacionalidad que desee filtrar: ")
    else:
        cadena = Ingresar_Tipo("\nIngrese el producto que desee filtrar: ")
    # Si el producto tiene la característica del filtro 
    for producto in lista:
        if producto[filtro] == cadena:
            nueva_lista.append(producto)
    return nueva_lista

def Menu_Filtros(lista):
    print("1. Filtrar por nacionalidad.")
    print("2. Filtrar por producto.")
    print("3. Filtrar por precio.")
    print("4. Volver al menú principal.")

    opcion = Ingresar_Opcion_Menu("\nIngrese la opción para filtrar: ", "Erro fuera de rango", 1, 4)

    if opcion == 1:
        # El código determina el filtro
        lista_filtro = Filtrar(lista, "nacionalidad", 1)
    elif opcion == 2:
        lista_filtro = Filtrar(lista, "tipo", 2)
    elif opcion == 3:
        Listar_Por_Precio(lista)
    
    if len(lista_filtro) > 0:
        Mostrar_Productos(lista_filtro)
    else:
        print("\nNo se encontraron productos con esas características.\n")

def Promedio(lista):
    suma = 0
    listado_nuevo = Filtrar(lista, "tipo", 2)
    # Recorro el listado filtrado
    if len(listado_nuevo) > 0:
        Mostrar_Productos(listado_nuevo)
        for producto in listado_nuevo:
            # Calculo el precio promedio
            suma += producto["precio"]
        promedio = suma / len(listado_nuevo)
        print(f"El promedio es: {promedio}$")
    else:
        print("\n\nNo hay productos en stock.\n")
            