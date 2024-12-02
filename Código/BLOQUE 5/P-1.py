# PROGRAMA 1. Impresión con formato.
# Fecha de elaboración:2024/11/13
# Elaborado por: Daniela Sahori Hinojosa Meza

nombre = "Edinguer"
edad = 26
calificacion = 93.8

# Impresión básica con concatenación
print("Mi nombre es: " + nombre + "\n Mi edad es: " + str(edad) )
print("Mi calificación es: " + str(calificacion))

print("\n")

# Impresión con f-strings
print("CADENAS DE TEXTOS FORMATEADAS")
# f(texto)
print(f"Nombre: {nombre}, edad: {edad}, promedio: {calificacion}")

print("\n")

# Impresión con formato usando %
print("UTILIZANDO EL CARÁCTER %")
print("Nombre: % s, edad %  d, promedio %.2f" % (nombre,edad, calificacion))