""" Adivina el número 

La computadora genera un número aleatorio entre 1 y 1000.
El usuario intenta adivinarlo.
"""
from random import randint
def intento():
    """Función que solicita un intento al usuario
    Returns:
        int: El número ingresado por el usuario
    """
    return int(input("Ingrese un número: "))
def juego(numeroInresado, numeroCorrecto):
    """Función que ejecuta el juego

    Args:
        numero (int): numero de intentos que le tomo a usuario para adivinar el numero
    """
    intentos = 0
    while numeroInresado != numeroCorrecto:
        if numeroInresado > numeroCorrecto:
            print("El número es menor")
        else:
            print("El número es mayor")
        numeroInresado = intento()
        intentos += 1
    return intentos
    
if '__main__' == __name__:
    numero_aleatorio = randint(1, 1000)
    numero_usuario =intento()
    intentos = juego(numero_usuario, numero_aleatorio)
    print(f"Felicidades, has adivinado el número en {intentos} intentos")

