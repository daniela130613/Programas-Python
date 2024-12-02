# PROGRAMA 7. Programa que filtra o clasifica las edades en una lista en los siguientes grupos:
# menores de 18, entre 18 y 65 y mayores de 65. El programa debe imprimir cuantas edades hay de cada grupo.
# Fecha de elaboración:2024/11/7
# Elaborado por: Daniela Sahori Hinojosa Meza

edades = [10, 15, 18, 8, 36,25, 67, 89, 95, 43, 26]
menore_18 = [] # Lista vacía para menores de 18.
adultos = [] # Lista vacía para adultos entre 18 y 65.
mayores_65 = [] # Lista vacía para mayores de 65.

for edad in edades:
    if edad < 18:
        menore_18.append(edad)
    elif edad >= 18 and edad <= 65:
        adultos.append(edad)
    else:
        mayores_65.append(edad)

print("\n \u2354 La lista de edades es:", edades)
print("\n \u2355 La lista de menores es:", menore_18)
print("\n \u2356 La lista de adulto es:", adultos)
print("\n \u2357 La lista de adultos mayores es:", mayores_65)