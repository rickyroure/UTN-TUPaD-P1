EDAD_MINIMA = 21

edad = int(input("Ingrese su edad: ")) 
categoria = input("Igrese su categoria(A, B, C, D, E, F, G): ")

if edad >= EDAD_MINIMA and (categoria == "D" or "d"):
    print("Prueba de conducir ambulancia")
else:
    print("No puede conducir ambulancia")
