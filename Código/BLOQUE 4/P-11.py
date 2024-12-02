# PROGRAMA 11. Programa que se repite hasta que ingrese la palabra 'salir'
# Fecha de elaboración:2024/11/08
# Elaborado por: Daniela Sahori Hinojosa Meza

# Inicialización de variables
palabra = " "
while palabra != "salir":
    palabra = input("Ingresa una palabra o 'salir' para terminar: ")
    palabra = palabra.lower()
    print("Usted ingresó: ", palabra)
print("Fin del programa")