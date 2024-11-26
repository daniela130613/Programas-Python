# Programa 7. Calcula el área y el perímetro de un círculo
# ingresando el valor del radio por el usuario
# Fecha de elaboración: 2024/10/15
# Elaborado por: Daniela Sahori Hinojosa Meza

# Área es A = π r²
# Perímetro es = π * d

radio = float(input("Ingrese el valor del radio: "))
areaCirculo = 3.1416 * radio ** 2
perimetroCirculo = 3.1416 * 2 * radio

print("El área del círculo es: " + str(areaCirculo))
print("El perímetro del círculo es: " + str(perimetroCirculo))
