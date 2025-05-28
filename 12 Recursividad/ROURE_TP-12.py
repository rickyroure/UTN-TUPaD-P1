#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
limite = int(input("Ingrese un número entero mayor o igual a 1: "))
if limite < 1:
    print("El número debe ser mayor o igual a 1.")
else:
    for i in range(1, limite + 1):
        print(f"Factorial de {i} es {factorial(i)}")

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
pos = int(input("Ingrese una posición (número entero mayor o igual a 0): "))
if pos < 0:
    print("La posición debe ser mayor o igual a 0.")
else:
    print(f"Serie de Fibonacci hasta la posición {pos}:")
    for i in range(pos + 1):
        print(fibonacci(i), end=" ")

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero no negativo): "))
if exponente < 0:
    print("El exponente debe ser un número entero no negativo.")
else:
    resultado = potencia(base, exponente)
    print(f"{base} elevado a la {exponente} es igual a {resultado}")

#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
    print("Debe ingresar un número entero positivo.")
elif numero == 0:
    print("El número binario es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
if es_palindromo(texto):
    print(f'"{texto}" es un palíndromo.')
else:
    print(f'"{texto}" no es un palíndromo.')

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
    print("Debe ingresar un número entero positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
nivel_inferior = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
if nivel_inferior < 1:
    print("Debe ingresar un número entero mayor o igual a 1.")
else:
    total = contar_bloques(nivel_inferior)
    print(f"Se necesitan {total} bloques para construir la pirámide.")

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito (0 a 9): "))
if numero < 0 or not (0 <= digito <= 9):
    print("Entrada inválida. El número debe ser positivo y el dígito entre 0 y 9.")
else:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")