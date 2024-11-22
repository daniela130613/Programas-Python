# Programas-Python
# Imprime un saludo

# Saludo en GitHub
def saludo_github(nombre_usuario):
    if nombre_usuario:
        print(f"¡Hola, @{nombre_usuario}! 👋 Bienvenido/a al repositorio. 🚀")
    else:
        print("¡Hola! 👋 No olvides personalizar tu nombre de usuario en GitHub. 😊")

# Solicita el nombre del usuario
usuario = input("Ingresa tu nombre de usuario de GitHub: ")
saludo_github(usuario)
