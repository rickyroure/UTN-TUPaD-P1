    #1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!|")

    #2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
    #el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
    #por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
    #realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

    #3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
    #imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
    #“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
    #años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
    #la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
edad = int(edad)
residencia = input("Ingrese su residencia: ")
print("Soy",nombre,apellido,", tengo",edad,"años y vivo en",residencia)

    #4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
    #su perímetro.
pi = 3.14
radio = float(input("Ingrese el radio: "))
area =  pi * radio ** 2
perimetro = 2 * pi * radio
print(area)
print(perimetro)

    #5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
    #cuántas horas equivale.
segundos = int(input("Ingrese la cantidad de segundos:"))
horas = segundos / 3600
print(f"Las horas equivalentes a {segundos} segundos es igual a {float(horas)} horas")

    #6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
    #multiplicar de dicho número.
numero = int(input("Ingrese un numero "))
print (f"{numero} X 1 = {numero * 1}")
print (f"{numero} X 2 = {numero * 2}")
print (f"{numero} X 3 = {numero * 3}")
print (f"{numero} X 4 = {numero * 4}")
print (f"{numero} X 5 = {numero * 5}")
print (f"{numero} X 6 = {numero * 6}")
print (f"{numero} X 7 = {numero * 7}")
print (f"{numero} X 8 = {numero * 8}")
print (f"{numero} X 9 = {numero * 9}")

    #7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
    #pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("Ingrese un numero entero distinto a 0: "))
num2 = int(input("Ingrese otro numero entero distinto a 0: "))
sum = num1 + num2
resta = num1 - num2
div = num1 / num2
mult = num1 * num2
print(f"suma {sum}")
print(f"resta {resta}")
print(f"division {div}")
print(f"multiplicacion {mult}")

    #8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
    #de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
altura = float(input("Ingrese tu altura: "))
peso = float(input("Ingrese tu peso: "))
masaCorporal = peso / altura ** 2
print(f"Su indice de masa corporal es {masaCorporal}")

    #9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
    #pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
celsius = int(input("Ingrese temperatura en grados celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit} °F")

    #10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
    #dichos números.
num1 = int(input("Ingrese el primer mumero: "))
num2 = int(input("Ingrese el segundo mumero: "))
num3 = int(input("Ingrese el tercer mumero: "))
promedio = (num1 + num2 + num3) / 3
print(f"EL promedio es {int(promedio)}")