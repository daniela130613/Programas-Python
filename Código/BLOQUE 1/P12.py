# PROGRAMA 12. Programa para probar las compuertas lógicas AND, OR y NOT
# 2024-10-18
# Elaborado por: Daniela Sahori Hinojosa Meza

#Tablas de verdad en compuertas lógicas
print("Tabla de verdad para la compuerta OR:")
print("-------------------------------------")
print("|  A  |  B  |  Q (A OR B) |")
print("-------------------------------------")
print("|  0  |  0  |      0      |")
print("|  0  |  1  |      1      |")
print("|  1  |  0  |      1      |")
print("|  1  |  1  |      1      |")
print("-------------------------------------")
print(False or False)
print(False or True)
print(True or False)
print(True or True)

print("\n Tabla de verdad para la compuerta AND:")
print("-------------------------------------")
print("|  A  |  B  |  Q (A AND B) |")
print("-------------------------------------")
print("|  0  |  0  |      0      |")
print("|  0  |  1  |      0      |")
print("|  1  |  0  |      0      |")
print("|  1  |  1  |      1      |")
print("-------------------------------------")
print( False and False)
print( False and True)
print( True and False)
print( True and True)

print("\n Tabla de verdad para la compuerta NOT:")
print("\n -----------------------")
print("|  A  |  Q (NOT A) |")
print("-----------------------")
print("|  0  |      1     |")
print("|  1  |      0     |")
print("-----------------------")

print(not False)
print(not True)
