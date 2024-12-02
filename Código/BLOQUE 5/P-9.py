# PROGRAMA 9. Decidir si un número entre 10 y 99 es primo. 
# El número lo ingresa el usuario.
# Fecha de elaboración:2024/11/15
# Elaborado por: Daniela Sahori Hinojosa Meza

num = int(input("Ingrese un número: "))

# Verificar si el número está en el rango [10, 99]
if 10 <= num <= 99:
    es_primo = True  # Asumimos que el número es primo
    
    for i in range(2, num):
        if num % i == 0:  # Si el número es divisible por i
            es_primo = False
            break  # No necesitamos seguir buscando divisores
    
    if es_primo:
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} no es primo.")
else:
    print(f"El número {num} no está en el rango de 10 a 99.")