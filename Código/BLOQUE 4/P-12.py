# PROGRAMA 12. Programa que se repite hasta que ingrese la palabra 'salir'
# Fecha de elaboración:2024/11/08
# Elaborado por: Daniela Sahori Hinojosa Meza

# Inicialización de variables
palabra = " "
while True:
    palabra = input("Ingresa una palabra o 'salir' para terminar: ")
    palabra = palabra.lower() # Convierte la palbra a minúscula
    print("Usted ingresó: ", palabra)
    if palabra == "salir":
        break
    
print("Fin del programa \U0001F601 \n")
print("!Hasta luego¡ \U0001F601 \n * 5")
