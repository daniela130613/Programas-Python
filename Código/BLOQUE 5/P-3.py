# PROGRAMA 3. Funciones con lisatslistas.
# Fecha de elaboración:2024/11/13
# Elaborado por: Daniela Sahori Hinojosa Meza

# Ejemplo de append
frutas = ["manzana", "pera", "uva"]
frutas.append("mango")
print(f"Lista después de append: {frutas}")

print("\n")

# Ejemplo de extend
frutas = ["manzana", "pera", "uva"]
frutas.extend(["fresa", "plátano"])
print(f"Lista después de extend: {frutas}")

print("\n")

# Ejemplo de insert
frutas = ["manzana", "pera", "uva"]
frutas.insert(1, "mango")
print(f"Lista después de insert: {frutas}")

print("\n")

# Ejemplo de remove
frutas = ["manzana", "pera", "uva", "pera"]
frutas.remove("pera")
print(f"Lista después de remove: {frutas}")

print("\n")

# Ejemplo de pop
frutas = ["manzana", "pera", "uva"]
elemento = frutas.pop(1)
print(f"Elemento eliminado: {elemento}")
print(f"Lista después de pop: {frutas}")

print("\n")

# Ejemplo de index
frutas = ["manzana", "pera", "uva"]
indice = frutas.index("pera")
print(f"El índice de 'pera' es: {indice}")


print("\n")

# Ejemplo de count
frutas = ["manzana", "pera", "uva", "pera"]
cantidad = frutas.count("pera")
print(f"'Pera' aparece {cantidad} veces en la lista")

print("\n")

# Ejemplo de sort
numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()
print(f"Lista ordenada: {numeros}")

print("\n")

# Ejemplo de reverse
frutas = ["manzana", "pera", "uva"]
frutas.reverse()
print(f"Lista invertida: {frutas}")

print("\n")

# Ejemplo de copy
frutas = ["manzana", "pera", "uva"]
copia = frutas.copy()
print(f"Copia de la lista: {copia}")

print("\n")

# Ejemplo de clear
frutas = ["manzana", "pera", "uva"]
frutas.clear()
print(f"Lista después de clear: {frutas}")

print("\n")

# Ejemplo de list comprehension
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(f"Cuadrados de {numeros}: {cuadrados}")