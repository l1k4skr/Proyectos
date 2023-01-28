""" 
se prohíbe el uso de las siguientes herramientas de programación:
- Importación de módulos (ej: fractions, math, numpy, pandas, os, etc.).
- Definición de funciones.
- Construcciones que usen las palabras reservadas try y except.
- Expresiones regulares.
- Ciclos for y listas por comprensión.
- Uso de strings con formato para imprimir, ya sea utilizando la sintaxis de llaves o de porcentaje.
- Los tipos de dato conjunto (set), tupla (tuple) y diccionario (dict).
- Programación orientada a objetos, es decir, definición de clases y métodos.
- El uso de las funciones eval y exec.


Durante la fase final de su entrenamiento antes de un importante duelo, un piloto de carreras del 
popular juego María Carting, de la famosa empresa Mintiendo™, debe mejorar el tiempo que tarda 
en recorrer un circuito establecido. Se sabe que, en la edición anterior de esta competencia, los 
tiempos registrados por los ganadores (en minutos, segundos y milisegundos) fueron:
Oro: 5:47,914
Plata: 6:01,013
Bronce: 6:03,607
A fin de evaluar su rendimiento, el piloto ha registrado los tiempos para las últimas n veces que ha 
completado el circuito, y ahora le ha solicitado ayuda a usted.
Construya un programa en Python que solicite al usuario la cantidad de veces que ha completado el 
circuito y luego, uno a uno, el tiempo registrado en cada recorrido. El programa debe mostrar por 
pantalla la siguiente información:
- El mejor tiempo.
- El peor tiempo.
- La cantidad de veces que logra marcas que le otorgarían cada medalla.
Adicionalmente, el corredor quiere tener su registro de tiempos ordenados, por lo que le solicita 
que el programa le muestre el listado de los tiempos ingresados en orden creciente.
Ejemplo:
Entrada:
n: 5
tiempo 1: 6:07,394
tiempo 2: 6:01,348
tiempo 3: 5:30,120
tiempo 4: 6:02,146
tiempo 5: 6:03,408
Salida:
Mejor tiempo: 5:30,120
Peor tiempo: 6:07,394
Oro: 1
Plata: 0
Bronce: 3
Tiempos ordenados:
5:30,120
6:01,348
6:02,146
6:03,408
6:07,394

"""
# Bienvenida
print("Bienvenido al programa de carreras de Maria Carting")
Oro = 5*60 + 47.914 # 5:47,914 
Plata = 6*60+1.13 # 6:01,013
Bronce = 6*60 + 3.607 # 6:03,607
# Ingreso de datos
n = int(input("Ingrese la cantidad de veces que ha completado el circuito: "))
contador = 0
tiempos = []
# Ingreso de tiempos
while contador < n:
    contador += 1
    print("Tiempo "+ str(contador) + ": ", end = "")
    tiempo = input()
    tiempo = tiempo.replace(",", ".")
    tiempo = tiempo.split(":")
    total = 0
    
    cnt = 0
    while cnt < len(tiempo):
        total += float(tiempo[cnt]) * 60 ** (len(tiempo) - cnt - 1)
        cnt += 1
    tiempos.append(total)
    
# Ordenamiento de tiempos
tiempos = sorted(tiempos)

# Salidas

# Mejor tiempo
mejor = tiempos[0]
tm = mejor // 60
seg = mejor - (tm * 60)
if int(seg) < 10:
    seg = "0" + str(round(seg, 3))
print("Mejor tiempo: " + str(int(tm)) + ":" + str(round(seg, 3)))

# Peor tiempo
peor = tiempos[-1]
ptm = peor // 60
seg = peor - (ptm * 60)
if int(seg) < 10:
    seg = "0" + str(round(seg, 3))
print("Peor tiempo: " + str(int(ptm)) + ":" + str(round(seg, 3)))

# Medallas
o = 0
p = 0
b = 0
cnt2 = 0
while cnt2 < len(tiempos):
    if tiempos[cnt2] <= Oro:
        o += 1
    elif tiempos[cnt2] <= Plata:
        p += 1
    elif tiempos[cnt2] <= Bronce:
        b += 1
    cnt2 += 1
print("Oro: " + str(o))
print("Plata: " + str(p))
print("Bronce: " + str(b))