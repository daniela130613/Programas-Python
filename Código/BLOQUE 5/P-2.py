# PROGRAMA 2. Funciones con números
# Fecha de elaboración:2024/11/13
# Elaborado por: Daniela Sahori Hinojosa Meza

# Ejemplo de abs
numero = -10
print(f"El valor absoluto de {numero} es {abs(numero)}")

print("\n")

# Ejemplo de int
decimal = 3.14
print(f"El valor entero de {decimal} es {int(decimal)}")

print("\n")

# Ejemplo de float
numero = "42"
print(f"El número {numero} como flotante es {float(numero)}")

print("\n")

# Ejemplo de bool
valor = 0
print(f"El valor booleano de {valor} es {bool(valor)}")

print("\n")

# Ejemplo de list
cadena = "Python"
print(f"La cadena '{cadena}' como lista es {list(cadena)}")

print("\n")

# Ejemplo de pow
base = 3
exponente = 4
print(f"{base} elevado a {exponente} es {pow(base, exponente)}")

print("\n")

# Ejemplo de len
lista = [1, 2, 3, 4, 5]
print(f"La longitud de la lista {lista} es {len(lista)}")

print("\n")

# Ejemplo de min
numeros = [3, 5, 1, 7, 9]
print(f"El valor mínimo de {numeros} es {min(numeros)}")

print("\n")

# Ejemplo de max
numeros = [3, 5, 1, 7, 9]
print(f"El valor máximo de {numeros} es {max(numeros)}")

print("\n")
# Ejemplo de round
numero = 3.14159
print(f"{numero} redondeado a 2 decimales es {round(numero, 2)}")
print("\n")

# Ejemplo de sum
numeros = [1, 2, 3, 4, 5]
print(f"La suma de {numeros} es {sum(numeros)}")

print("\n")

# Ejemplo de sorted
numeros = [3, 5, 1, 7, 9]
print(f"La lista {numeros} ordenada es {sorted(numeros)}")

print("\n")
# Ejemplo de reversed
cadena = "Python"
print(f"La cadena '{cadena}' invertida es {''.join(reversed(cadena))}")
print("\n")

# Ejemplo de zip
nombres = ["Ana", "Juan", "Sofía"]
edades = [25, 30, 22]
print(f"Parejas nombre-edad: {list(zip(nombres, edades))}")

print("\n")

# Ejemplo de enumerate
frutas = ["manzana", "pera", "uva"]
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

print("\n")

# Ejemplo de all
valores = [True, True, False]
print(f"¿Todos los valores en {valores} son True? {all(valores)}")

print("\n")

# Ejemplo de any
valores = [False, False, True]
print(f"¿Algún valor en {valores} es True? {any(valores)}")