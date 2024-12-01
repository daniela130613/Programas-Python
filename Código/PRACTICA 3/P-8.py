# Programa 8. Programa que calcule el promedio de 5 unidades e indique si aprovó la materia.
# gracias por participar
# Fecha de elaboración:2024/10/24
# Elaborado por: Daniela Sahori Hinojosa Meza

u1 = int(input("Ingresa la calificación de la primera unidad:   "))
u2 = int(input("Ingresa la calificación de la segunda unidad:   "))
u3 = int(input("Ingresa la calificación de la tercera unidad:   "))
u4 = int(input("Ingresa la calificación de la cuarta unidad:   "))
u5 = int(input("Ingresa la calificación de la quinta unidad:   "))

promedio = (u1 + u2 + u3 + u4 + u5) / 5

if promedio >=8:
    print("Aprobó la materia con:  " + str(promedio))
else:
    print("Reprobó la materia con:  " + str(promedio))

print("Gracias por participar ")
