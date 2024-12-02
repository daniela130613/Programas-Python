# PROGRAMA 11. Afregue a el Programa 10 un ciclo while para que se repita el programa hasat que se 
# ingrese la palabra "salir" (esta puede estar en mayúsculas, minúsculas o ambas. )
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

# Ciclo while para repetir el programa hasta que se ingrese "salir"
while True:
    # Solicitar al usuario que ingrese un número o "salir"
    entrada = input("Ingrese un número entre 10 y 99 o escribe 'salir' para terminar: ").strip().lower()

    # Verificar si el usuario desea salir
    if entrada == "salir":
        print("¡Programa terminado!")
        break

    # Intentar convertir la entrada a un número
    try:
        num = int(entrada)
        
        # Verificar si el número está en el rango de 10 a 99
        if 10 <= num <= 99:
            # Llamar a la función para verificar si es primo
            resultado = es_primo(num)
            print(resultado)
        else:
            print(f"El número {num} no está en el rango de 10 a 99.")
    
    except ValueError:
        print("Por favor, ingrese un número válido o 'salir' para terminar.")