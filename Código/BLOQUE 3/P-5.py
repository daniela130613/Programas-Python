#PROGRAMA 5. Programa que calcule el nivel de desempeño de un estudiante respecto con su calificación 
# dada por el usuario, dada la siguiente tabla.
# Menos de 60      |  Insuficiente
# 70 - 79          |  Suficiente
# 80 - 89          |  Muy bien
# 90 - 95          |  Notable
# 96 - 100         |  Excelente
# Fecha de elaboración:2024/10/29
# Elaborado por: Daniela Sahori Hinojosa Meza

calificacion = input("¿Cuál es su calificación? ")
calificacion = float(calificacion)

if calificacion <= 60:
    print("Insuficiente")
elif calificacion >= 70 and calificacion <= 79:
    print("Suficiente")
elif calificacion >= 80 and calificacion <= 89:
    print("Muy bien")
elif calificacion >= 90 and calificacion <= 95:
    print("Notable")
else:
    print("Excelente")

print("¡Gracias por usar mi programa!")
