import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def main():
    print("Bienvenido al generador de contraseñas")

    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña (mínimo 6): "))
            if longitud < 6:
                print("Error: La longitud debe ser mayor o igual a 6")
                continue
        except ValueError:
            print("Error: Ingrese un número válido")
            continue

        contraseña = generar_contraseña(longitud)
        print(f"\nContraseña generada: {contraseña}")

        guardar = input("¿Desea guardar la contraseña? (responda con 'si' o 'no'): ").strip().lower()
        if guardar == 'si':
            with open("contraseñas_guardadas.txt", "a") as archivo:
                archivo.write(contraseña + "\n")
            print("Contraseña guardada en archivo.\n")

        otra = input("¿Desea generar una nueva contraseña? (responda con 'si' o 'no'): ").strip().lower()
        if otra != 'si':
            break

    print("Fin del programa.")

if __name__ == "__main__":
    main()