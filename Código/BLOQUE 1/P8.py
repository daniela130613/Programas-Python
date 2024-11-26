# Programa 8. Programa que calcule el número de minutos, horas y meses, dado el número de días por el usuario
# Fecha: 2024-10-16
# Elaborado por: Daniela Sahori Hinojosa Meza

dias = float(input("Ingresa el número de días: "))
horas = dias * 24
minutos = horas * 60
meses = dias / 30
print("El total de horas es: " + str(horas))
print("El total de minutos es: " + str(minutos))
print("El total de meses es: " + str(meses))
