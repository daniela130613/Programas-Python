# Programa 9. Programa que calcule el costo total de un número de artículos si:
# Son 3 artículos o menos precio unitario: $45.00
# Más de 3 artículos precio unitario: $30
# Fecha de elaboración:2024/10/25
# Elaborado por: Daniela Sahori Hinojosa Meza

cantidad = int(input("Ingresa la cantidad de artículos:   "))

if cantidad>3:
    total = cantidad * 30

else:
    total =cantidad * 45
print("EL total a pagar es: $ " + str(total))

print("Gracias por su compra ")
