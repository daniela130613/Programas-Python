# PROGRAMA 7. Agregue un ciclo for a programa 6 par indicarle cuántas veces debe realizar las operaciones.
# En cada iteración los números que se pasrán en los argumentos serán el doble que el anterior.
# Fecha de elaboración:2024/11/14
# Elaborado por: Daniela Sahori Hinojosa Meza

# Función que realiza operaciones matemáticas básicas
def operaciones(num1, num2, digitos):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = float(num1 / num2)
    modulo = num1 % num2
    print(f"La suma de {num1} + {num2} es: {suma} \n")
    print(f"La resta de {num1} - {num2} es: {resta} \n")
    print(f"La multiplicación de {num1} * {num2} es: {multiplicacion} \n")
    print(f"La división de {num1} / {num2} es: {division:.{digitos}f} \n")
    print(f"El módulo de {num1} % {num2} es: {modulo} \n")

# Solicitar datos al usuario
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
digitos = int(input("Ingresa la cantidad de decimales a mostrar en la división: "))
iteraciones = int(input("¿Cuántas veces quieres realizar las operaciones?: "))

# Ciclo for para repetir las operaciones
for i in range(iteraciones):
    print(f"\n--- Iteración {i + 1} ---")
    operaciones(num1, num2, digitos)
    num1 *= 2  # Duplica el valor del primer número
    num2 *= 2  # Duplica el valor del segundo número