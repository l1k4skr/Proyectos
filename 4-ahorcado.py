""" Ahorcado

En el juego intervienen dos jugadores, el que conoce la palabra secreta y el que tiene que adivinarla. Vamos a llamarlos, respectivamente, 
Guardián y Jugador. Así, Guardián es el que conoce la palabra secreta y el que va dibujando las letras y el ahorcado y Jugador el que intenta averiguarla.

Los eventos que van sucediendo en el juego son los siguientes:

Comienza el juego y Guardián piensa o elije una palabra secreta.
Guardián dibuja la horca.
Guardián dibuja tantas líneas como letras tiene la palabra secreta.
Jugador dice una letra.
Guardián comprueba la letra.
Si la letra está en la palabra, Guardián escribe la letra sobre las líneas correspondientes.
Si la letra no está en la palabra, Guardián la escribe como letra utilizada y dibuja una parte del ahorcado en la horca.
Si se ha completado la palabra, el juego termina y Jugador gana.
Si se ha completado el dibujo del ahorcado, el juego termina y Jugador pierde.
Si no se han completado ni el dibujo ni la palabra se vuelve al paso 4.
"""
palabra = 'Hola'#input("Escribe una palabra: ")
respuesta = ("_ " * len(palabra))
respuesta = respuesta[:-1]
respuesta = respuesta.split(" ")
while "".join(respuesta) != palabra:
    print(" ".join(respuesta))
    letra = input("Escribe una letra: ")
    if len(letra) < 2:
        if letra in palabra:
            indice = palabra.index(letra)
            respuesta[indice] = letra
    else:
        for i in letra:
            if i in palabra:
                indice = palabra.index(i)
                respuesta[indice] = i

print(" ".join(respuesta))
print("Felicidades, has adivinado la palabra")