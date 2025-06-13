# Ejercicio 1:

#  1) Dado el diccionario precios_frutas
#  precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#  Añadir las siguientes frutas con sus respectivos precios:
#  ● Naranja = 1200
#  ● Manzana = 150

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

precios_frutas ["Naranja"] = '1200'
precios_frutas ["Manzana"] = '150'
precios_frutas ["Pera"] = '2300'



print(precios_frutas)

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 2:

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas ["Banana"] = '1330'
precios_frutas ["Manzana"] = '1700'
precios_frutas ["Melon"] = '2800'

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

frutas = list(precios_frutas.keys())
print(frutas)

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 4:

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

# Diccionario vacio para almacenar datos.
agenda = {}

print("CARGA DE CONTACTOS:")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto #{i+1}: ")
    numero = input(f"Ingresá el numero telefonico de {nombre}: ")
    agenda[nombre] = numero

# # Consultar un contacto
print("\nCONSULTA DE NUMERO TELEFONICO:")
nombre_buscado = input("Ingresa el nombre del contacto a buscar: ")

if nombre_buscado in agenda:
    print(f"El numero de {nombre_buscado} es {agenda[nombre_buscado]}")
else:
    print(f"No se encontro ningun contacto con el nombre '{nombre_buscado}'.")

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 5:

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresa una frase")

palabras = frase.lower().split()

# Obtener palabras unicas
palabras_unicas = set(palabras)
print("\nPalabras únicas:")
print(palabras_unicas)

 # Contar cantidad de veces que aparece cada palabra
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1


print("\nCantidad de apariciones de cada palabra:")
for palabra, cantidad in contador_palabras.items(): # Permite recorrer dentro del bucle for items del diccionario y mostrarlos en print
    print(f"{palabra}: {cantidad}")

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 6:

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

# Diccionario vacio para guardar los alumnos y sus notas
alumnos = {}

# # Cargamos los datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = []

    for j in range(3):
        nota = float(input(f"Ingresá la nota {j+1} de {nombre}: "))
        notas.append(nota)

    alumnos[nombre] = tuple(notas)  # Guardar las notas como tupla

# Calcular y mostrar el promedio de cada alumno
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 7:

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 8:

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

# Diccionario con productos y su stock inicial
stock_productos = {
    "manzanas": 10,
    "naranjas": 15,
    "bananas": 5
}

# Menu principal
while True:
    print("\n--- MENU DE STOCK ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un producto nuevo")
    print("4. Ver todos los productos y su stock")
    print("5. Salir")
    
    opcion = input("Elegir una opcion (1-5): ")
    
    if opcion == "1":
        producto = input("Ingresar nombre del producto: ").lower()
        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print("El producto no existe en el sistema.")
    
    elif opcion == "2":
        producto = input("Producto al que queres agregar unidades: ").lower()
        if producto in stock_productos:
            agregar = int(input("Cuantas unidades queres agregar?: "))
            stock_productos[producto] += agregar
            print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print("El producto no existe. Primero agregalo como nuevo.")
    
    elif opcion == "3":
        producto = input("Nombre del nuevo producto: ").lower()
        if producto in stock_productos:
            print("Ese producto ya existe.")
        else:
            nuevo_stock = int(input("Stock inicial del nuevo producto: "))
            stock_productos[producto] = nuevo_stock
            print(f"{producto} agregado con {nuevo_stock} unidades de stock.")
    
    elif opcion == "4":
        print("\n--- LISTA DE PRODUCTOS ---")
        for prod, stock in stock_productos.items():
            print(f"{prod}: {stock} unidades")
    
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opcion invalida. Elegi una del 1 al 5.")

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 9:

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

# # Creo un diccionario donde la clave es una tupla (dia, hora) y el valor es el evento
agenda = {
    ("lunes", "10:00"): "Reunion con equipo",
    ("martes", "14:00"): "Clase de ingles",
    ("viernes", "18:30"): "Gimnasio"
}

 # Pido al usuario que ingrese el dia y la hora
dia = input("Ingresar dia (ej: lunes): ").lower()
hora = input("Ingresar hora (ej: 10:00): ")

 # Armo la tupla con el dia y la hora ingresados
clave = (dia, hora)

 # Consulto si existe un evento en ese dia y hora
if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay actividades en ese dia y hora.")

#------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 10:

def invertir_diccionario(diccionario_original):
    return {capital: pais for pais, capital in diccionario_original.items()}

 # Diccionario de ejemplo (puedes reemplazarlo con uno más grande)
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Francia": "Paris",
    "Japon": "Tokio",
    "Alemania": "Berlin",
    "Italia": "Roma",
    "España": "Madrid"
}

capitales_paises = invertir_diccionario(paises_capitales)

print("Diccionario original:")
print(paises_capitales)

print("\nDiccionario invertido:")
print(capitales_paises)