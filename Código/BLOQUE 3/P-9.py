#PROGRAMA 9. Igualdad en listas.
#Compare puntos con todos las demás listas para comprobar si son iguales o diferentes.
# Fecha de elaboración:2024/10/31
# Elaborado por: Daniela Sahori Hinojosa Meza

puntos = [10, 30, 20]
puntos_2 = [10, 30, 20]
ordenados = [10, 20, 30]
puntos_texto = ["10", "20", "30"]

print (puntos == puntos_2) # True
print (puntos == ordenados) # False
print (puntos == 10, 20, 30) # False

print (puntos != puntos_2) # False
print (puntos != ordenados) # True
print (puntos != puntos_texto) # True