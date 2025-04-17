#for x in range(1,11,2):
#    print(f"{x}")

#umbral = 10
#sumatoria = 0
#cont = 0

#while sumatoria < umbral:
#    cont += 1
#    num = int(input("Ingrese un numero: "))
#    sumatoria += num
    

#print("El primedio es",(sumatoria / cont))

#cant_numeros = 5
#sumatoria = 0

#for cont in range(1,cant_numeros+1):
#    print("Ingrese numero",cont)
#    num = int(input())
#    sumatoria += num
#    print()

#print("La sumatoria de los valores es",sumatoria)
#print("El primedio",(sumatoria/cant_numeros))

sueldoAnual = 0

for contMeses in range(1,13):
    print("Ingrese su sueldo para el mes n°",contMeses)
    sueldoMensual = float(input())
    sueldoAnual+= sueldoMensual

print("Su sueldo anual es" ,sueldoAnual)
