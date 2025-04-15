for x in range(1,11,2):
    print(f"{x}")

umbral = 10
sumatoria = 0
cont = 0

while sumatoria < umbral:
    cont += 1
    num = int(input("Ingrese un numero: "))
    sumatoria += num
    

print("El primedio es",(sumatoria / cont))