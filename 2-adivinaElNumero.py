""" Adivina el número 

La computadora genera un número aleatorio entre 1 y 1000.
El usuario intenta adivinarlo.
"""
import random

numero_aleatorio = random.randint(1, 1000)
numero_usuario = int(input("Adivina el número: "))
while numero_usuario != numero_aleatorio:
    if numero_usuario > numero_aleatorio:
        print("El número es menor")
    else:
        print("El número es mayor")
    numero_usuario = int(input("Adivina el número: "))
print("Felicidades, has adivinado el número")

