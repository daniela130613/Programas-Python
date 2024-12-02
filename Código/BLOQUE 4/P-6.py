# PROGRAMA 6. Programa que permita crear una lista de todos los números menores a 50.
# Fecha de elaboración:2024/11/06
# Elaborado por: Daniela Sahori Hinojosa Meza

print("The filter pattern (FILTROS)\n")

numeros = [10, 50, 25, 13, 10, 28, 100, 500, 29, 29]
menores_50 = [] # Crea una lista nueva
for numero in numeros:
    if numero < 50:
        menores_50.append(numero)

print("La lista original es:", numeros)
print("La nueva lista es:", menores_50)