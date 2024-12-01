# Programa 10A. Revisar si puedes ver una película en Netflix.
# La condición para esto es que seas mayor de edad y que haya s comprado la película.
# if anidados
# Fecha de elaboración:2024/10/25
# Elaborado por: Daniela Sahori Hinojosa Meza

edad = int(input("¿cuántos años tienes?:   "))


if edad >= 18:
    compra =int(input("¿Compraste la película?\n 0-NO \n 1-SI\n  "))
    if compra == 1:
        print("Puede ver la película")  

else:
    print("Vete a hacer la tarea")

print("¡Gracias por usar Netflix!")
