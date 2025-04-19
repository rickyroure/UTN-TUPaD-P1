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

import random
numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adiviná el número (entre 0 y 9): "))
    intentos += 1

    if intento == numero_secreto:
        adivinado = True
        print(f"¡Correcto! El número era {numero_secreto}. Lo adivinaste en {intentos} intento(s).")
    else:
        print("No es ese, intentá de nuevo.")