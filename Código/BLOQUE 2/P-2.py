# PROGRAMA 2. Programa que si Chorchis o Choto van a la fiesta,
# entonces no hay fiesta.
# Fecha de elaboración:2024/10/22
# Elaborado por: Daniela Sahori Hinojosa Meza



print("-------------------------------------")
print("|  Chr  |  Cho  |  Fiesta NOT(OR) |")
print("-------------------------------------")
print("|  0    |  0    |      1          |")
print("|  0    |  1    |      0          |")
print("|  1    |  0    |      0          |")
print("|  1    |  1    |      0          |")
print("-------------------------------------")

print(not(False or False)) # Si hay fiesta
print(not(False or True)) # No hay fiesta
print(not(True or False)) # No hay fiesta
print(not(True or True)) # No hay fiesta