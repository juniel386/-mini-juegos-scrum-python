
import random

colores = ["Rosa", "Amarillo", "Verde", "Azul", "Rojo", "Morado", "Naranja", "Negro", "Violeta"]

color_seleccionado = "Rosa"  
print("Bienvenido al juego 'Adivina el Color'!")
print("Tengo en mente un color. Intenta adivinar cuál es.")

adivinaste = False

while not adivinaste:
    suposicion = input("Ingresa un color: ").capitalize()  

    if suposicion == color_seleccionado:
        print("¡Felicidades! Adivinaste el color.")
        adivinaste = True
    else:
        print("¡Incorrecto! Intenta de nuevo.")