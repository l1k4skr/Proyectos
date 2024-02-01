"""Quiero empezar a desarrollar un programa en python que me permita analizar un disco duro.
Entre las funciones que quiero desarrollar esta:
  - Listar archivos pesados
  - Organizar en tipos de archivos (Fotos, Videos, archivos, etc) de mas pesado a menos
  - Quiero que el programa me recomiende borrar archivos grandes que esten en desuso o que no se hayan ocupado en un largo tiempo
  - Cualquier funcionalidad que se te ocurra para optimizar el espacio en mi disco duro
"""
import os

def listar_archivos(rute, weigth=False):
    rute = os.path.abspath(rute)
    for file in os.listdir(rute):
        if file[0] == ".":
            continue
        if weigth:
            rute = os.path.join(rute, file)
            print(f"{file} - {os.path.getsize(rute)}")
        else:
            print(file)
        
def organizar_archivos():
    pass

def borrar_archivos():
    pass


listar_archivos("..", weigth=True)
