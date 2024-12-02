# PROGRAMA 1. BLOQUE ELIF
# Fecha de elaboración:2024/10/28
# Elaborado por: Daniela Sahori Hinojosa Meza
# else + if : elif

mascota = input("Ingresa el tipo de mascota que tienes: ") # Pregunta si la palabra "perro"está dentro de la 
if "perro" in mascota:                                     # variable "mascota"
      print("Es un perro")
elif "gato" in mascota:                   # Es un else + if fusionado
    print("Tienes un gato")
else:
    print("Mascota desconocida")

print("Gracias por usar nuestro programa")   