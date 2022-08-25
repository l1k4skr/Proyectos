"""
1. Definir una historia. 
    - "Había una vez una mujer que se llamaba {Nombre}. {Nombre} tenia muy {ad1} su(s) {parte_cuerpo}.Un dia, {Nombre} le dijo a su {ad2} {relaciónPersonal}: "Hola, {relaciónPersonal}, como estás?, a lo que {relaciónPersonal} respondió: "Muy bien, y tu, {Nombre}?.
2. Establecer variables para cada parte de la historia.
    - Nombre, ad1, ad2, parte_cuerpo, relaciónPersonal.
3. Imprimir la historia.
"""

print('Bienvenido a Historias Locas')
print('Te solicitaremos que ingreses algunos datos')
genero = input('Escoge un genero su genero(Hombre/Mujer):  ').lower()
if genero != 'hombre' and genero != 'mujer':
    genero = 'hombre'
if genero == 'hombre':
    conjugar = 'un'
else:
    conjugar = 'una'
nombre = input("¿Elige un nombre?: ")
ad1 = input("Define un adjetivo: ")
ad2 = input("Define otro adjetivo: ")
parte_cuerpo = input("Define una parte del cuerpo: ")
rP = input("Define una relación personal: ")

print(f"Había una vez {conjugar} {genero} que se llamaba {nombre}. {nombre} tenia muy {ad1} su(s) {parte_cuerpo}. Un dia, {nombre} le dijo a su {ad2} {rP}: \"Hola, {rP}, como estás?, a lo que {rP} respondió: \"Muy bien, y tu, {nombre}?\", luego el mundo estallo.")