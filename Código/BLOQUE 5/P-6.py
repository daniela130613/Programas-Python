# PROGRAMA 6. Crea una función dentro de un programa que imprima las siguientes operaciones: 
# suma, resta, multiplicación, división y módulo.
# Fecha de elaboración:2024/11/14
# Elaborado por: Daniela Sahori Hinojosa Meza

# Función que realiza operaciopnes matemáticas básicas
def operaciones(num1, num2, digitos):
    suma  = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = float(num1 / num2)
    modulo = num1 % num2
    print(f"\n La suma de {num1} + {num2} es: {suma} \n \n")
    print(f"La resta de {num1} - {num2} es: {resta} \n \n")
    print(f"La multiplicación de {num1} * {num2} es: {multiplicacion} \n \n")
    print(f"La división de {num1} / {num2} es: {division:.{digitos}f} \n \n")
    print(f"El módulo de {num1} % {num2} es: {modulo} \n \n")

# Solicitar datos al usuario
num2 = int(input("Ingresa el segundo número: "))
num1 = int(input("Ingresa el primer número: ")) 
digitos = int(input("Ingresa la cantidad de decimales a mostrar en la división y módulo: "))

operaciones(num1, num2, digitos)
operaciones(140, 8, 5)