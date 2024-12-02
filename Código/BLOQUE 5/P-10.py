# PROGRAMA 10. Crear una función para que cada vez que se llame, dando como argumento el número ingresado por el usuario,
# calcule si es primo o no.
# El número lo ingresa el usuario.
# Fecha de elaboración:2024/11/15
# Elaborado por: Daniela Sahori Hinojosa Meza

# Función que determina si un número es primo
def es_primo(num):
    # Verificar si el número es primo
    if num < 2:
        return f"El número {num} no es primo."
    
    for i in range(2, num):
        if num % i == 0:
            return f"El número {num} no es primo."
    
    return f"El número {num} es primo."

# Solicitar al usuario que ingrese un número
num = int(input("Ingrese un número entre 10 y 99: "))

# Verificar si el número está en el rango
if 10 <= num <= 99:
    # Llamar a la función para verificar si es primo
    resultado = es_primo(num)
    print(resultado)
else:
    print(f"El número {num} no está en el rango de 10 a 99.")