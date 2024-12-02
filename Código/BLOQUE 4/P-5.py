# PROGRAMA 5. Patron para contar. The count pattern. Patrones para ciclos (Loops patterns)
# Fecha de elaboración:2024/11/05
# Elaborado por: Daniela Sahori Hinojosa Meza

print("Patrones para ciclos (Loops patterns)\n")

letras= ["a", "b", "c", "d", "e"]
contador =  0   #Inicializa variable
for letra in letras:
    contador = contador + 1
    print("La lista \n""letras""\n tiene", contador, "letras")
           

print("\n")

print("The sum pattern \n")
numeros=[100, 200, 300, 400]
sumatoria = 0 #Inicializa variable
for numero in numeros:
    sumatoria = sumatoria + numero
    print("La sumatoria es", sumatoria)

print("\n")

print("The accumulation pattern \n")
palabras = ["Hoy", " ", "hace", " ", "frío"]
mensaje = ""    # Inicializa variable
for palabra in palabras:
    mensaje = mensaje + palabra

print("\n")

print("The map pattern \n")
lista_anterior = ["Manzana", "Piña", "Uva"]
lista_nueva = []
print("La lista vacía", lista_nueva)
for fruta in lista_anterior:
    lista_nueva.append(fruta)
    print("La lista copiada  es", lista_nueva)