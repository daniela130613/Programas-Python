# PROGRAMA 2. Programa que indique si, de dos enteros ingresados, el primero es mayor, 
# igual o menor que el segundo.
# Fecha de elaboración:2024/10/28
# Elaborado por: Daniela Sahori Hinojosa Meza

n1 = input("Ingresa el primer número: ")
n1 = int(n1) # Convierte el entero string ingresado desde el teclado

n2 = int(input("Ingresa el segundo número: ")) # También pedo convertir un entero de esta forma.

if (n1>n2):
    print(str(n1) + " es mayor que " + str(n2))
elif n1 == n2:
    print(str(n1) + " es igual que " + str(n2))
else:
    print(str(n1) + " es menor que " + str(n2))

print("¡Gracias por usar mi programa!")
