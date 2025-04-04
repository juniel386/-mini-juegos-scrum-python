import random

def elegir_palabra():
    palabras = ['gerok', 'lluvia', 'juego', 'adivinar', 'consola', 'familia']
    return random.choice(palabras)

def jugar():
    palabra = elegir_palabra()
    letras_adivinadas = []
    intentos = 6
    palabra_oculta = '_' * len(palabra)

    print("¡Bienvenido al juego de adivinar la palabra!")
    
    while intentos > 0 and '_' in palabra_oculta:
        print("\nPalabra: ", ' '.join(palabra_oculta))
        print(f"Tienes {intentos} intentos restantes.")
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print("¡Correcto!")
            palabra_oculta = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
        else:
            intentos -= 1
            print("Incorrecto. Pierdes un intento.")

    if '_' not in palabra_oculta:
        print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
    else:
        print(f"¡Has perdido! La palabra era: {palabra}")

if __name__ == "__main__":
    jugar()