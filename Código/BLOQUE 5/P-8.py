# PROGRAMA 8. Agregue a programa 7 un ciclo while para que se repita el programa hasta que se ingrese la palabra
# "salir" (esta puede estar en mayúsculas, minúsculas o con ambas)
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

# Ciclo principal del programa
while True:
    # Solicitar datos al usuario
    comando = input("Escribe 'salir' para terminar o presiona ENTER para continuar: ").strip().lower()
    if comando == "salir":
        print("¡Programa terminado!")
        break
    
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    digitos = int(input("Ingresa la cantidad de decimales a mostrar en la división: "))
    iteraciones = int(input("¿Cuántas veces quieres realizar las operaciones?: "))

    # Ciclo for para realizar las operaciones
    for i in range(iteraciones):
        print(f"\n--- Iteración {i + 1} ---")
        operaciones(num1, num2, digitos)
        num1 *= 2  # Duplica el valor del primer número
        num2 *= 2  # Duplica el valor del segundo número