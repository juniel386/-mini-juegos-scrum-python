def adivina_el_numero():
    print("\nJuego: Adivina el número")
    # Aquí agregarías la lógica para el juego "Adivina el número"

def adivina_el_color():
    print("\nJuego: Adivina el color")
    # Aquí agregarías la lógica para el juego "Adivina el color"

def juego_de_dados():
    print("\nJuego: Juego de dados")
    # Aquí agregarías la lógica para el juego "Juego de dados"

def piedra_papel_o_tijeras():
    print("\nJuego: Piedra, papel o tijeras")
    # Aquí agregarías la lógica para el juego "Piedra, papel o tijeras"

def main():
    while True:
        print("\nBienvenido al sistema de juegos")
        print("1. Adivina el número")
        print("2. Adivina el color")
        print("3. Juego de dados")
        print("4. Piedra, papel o tijeras")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            adivina_el_numero()
        elif opcion == "2":
            adivina_el_color()
        elif opcion == "3":
            juego_de_dados()
        elif opcion == "4":
            piedra_papel_o_tijeras()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor selecciona una opción entre 1 y 5.")

if __name__ == "__main__":
    main()