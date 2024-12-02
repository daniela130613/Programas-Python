# PROGRAMA 9. Programa que muestra el uso de los comandos \"break\" y \"continue\"  
# Fecha de elaboración:2024/11/08
# Elaborado por: Daniela Sahori Hinojosa Meza

# Ejemplo 1 - break
# Imprimir los números del 1 al 10,
# pero si el número es 5, salir del
# ciclo while

i = 1
while i <= 10:
    if i == 5:
         break
    print(i)
    i += 1 # Equivalente a i = i + 1
print("Fin del programa")

# Ejemplo 2 - continue
# Imprimir los números del 1 al 10,
# pero si el número es 5, omitirlo

i = 1
while i <= 10:
    if i == 5:
         i += 1
         continue
    print(i)
    i += 1 # Equivalente a i = i + 1
print("Fin del programa")