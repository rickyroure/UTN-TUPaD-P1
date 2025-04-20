#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#for num in range(101):
#    print(num)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene

#numero = int(input("Ingrese un número entero: "))
#cantidad_digitos = len(str(abs(numero)))
#print("El número tiene", cantidad_digitos, "dígito(s).")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

#num_inicio = int(input("Ingrese el primer numero: "))
#num_fin = int(input("Ingrese el segundo numero: "))

#menor = min(num_inicio,num_fin)
#mayor = max(num_inicio,num_fin)

#suma = 0

#for i in range(menor+1,mayor):
#    suma += i

#print(f"La suma entre los numeros comprendidos entre {menor} y {mayor} es {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

#numero = int(input(f"Ingrese numeros (0 para cortar): "))
#suma_num = numero
#while numero != 0:
#    numero = int(input(f"Ingrese numeros (0 para cortar): "))
#    suma_num += numero

#print(f"La suma es {suma_num}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#import random

#numero_aleatorio = random.randint(0, 9)
#intentos = 0
#adivinado = False

#while not adivinado:
#    intento = int(input("Adiviná el número (entre 0 y 9): "))
#    intentos += 1

#    if intento == numero_aleatorio:
#        adivinado = True
#        print(f"¡Correcto! El número era {numero_aleatorio}. Lo adivinaste en {intentos} intento(s).")
#    else:
#        print("No es ese, intentá de nuevo.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

#for num in range(100,-1,-1):
#    if num % 2 == 0:
#        print(num)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

#numero = int(input("Ingrese un número entero positivo: "))
#suma = 0
#for i in range(numero + 1):  # Incluye el número ingresado
#    suma += i

#print("La suma de los números desde 0 hasta", numero, "es:", suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Cantidad de números a ingresar (podés cambiarlo para probar)
#total_numeros = 100

#pares = 0
#impares = 0
#positivos = 0
#negativos = 0

#for i in range(total_numeros):
#    numero = int(input(f"Ingrese el número {i+1}: "))

#    if numero % 2 == 0:
#        pares += 1
#    else:
#        impares += 1

#    if numero > 0:
#        positivos += 1
#    elif numero < 0:
#        negativos += 1

#print("Cantidad de números pares:", pares)
#print("Cantidad de números impares:", impares)
#print("Cantidad de números positivos:", positivos)
#print("Cantidad de números negativos:", negativos)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

#total_numeros = 100  

#suma = 0

#for i in range(total_numeros):
#    numero = int(input(f"Ingrese el número {i+1}: "))
#    suma += numero

#media = suma / total_numeros

#print("La media de los números ingresados es:", media)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = input("Ingrese un número: ")

numero_invertido = numero[::-1]

print("Número invertido:", numero_invertido)
