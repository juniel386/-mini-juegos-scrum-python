import random


def lanzar_dado():
    return random.randint(1, 6)


def juego_dados():
    print("🎲 ¡Bienvenido al Juego de Dados! 🎲")
    print("1. Lanzar un dado")
    print("2. Jugar contra la computadora")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(f"Has lanzado el dado y salió: {lanzar_dado()} 🎲")
    elif opcion == "2":
        jugador = lanzar_dado()
        computadora = lanzar_dado()
        print(f"Tú sacaste {jugador} 🎲 | La computadora sacó {computadora} 🎲")
        if jugador > computadora:
            print("🎉 ¡Ganaste! 🎉")
        elif jugador < computadora:
            print("😢 Perdiste, la computadora ganó.")
        else:
            print("🤝 ¡Empate!")
    elif opcion == "3":
        print("Saliendo del juego...")
    else:
        print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    juego_dados()
