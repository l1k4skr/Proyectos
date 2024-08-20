'''
Proyecto: Gestión de Contactos

Descripción
El proyecto consiste en un sistema de gestión de contactos donde cada contacto tiene un nombre, un número de teléfono y una lista de etiquetas (por ejemplo, "amigo", "trabajo", "familia"). El sistema debería permitirte agregar, eliminar, y buscar contactos, así como listar todos los contactos agrupados por etiquetas.

Estructuras de Datos a Utilizar
Lista: Para almacenar todos los contactos.
Tupla: Para representar un contacto individual (nombre y teléfono).
Diccionario: Para almacenar detalles adicionales de los contactos, como las etiquetas.
Set: Para almacenar y gestionar las etiquetas, asegurando que no haya duplicados.

Funcionalidades
Agregar Contacto: Permite al usuario agregar un nuevo contacto a la lista. Cada contacto es una tupla que contiene un nombre y un número de teléfono, y se asocia a un diccionario que contiene las etiquetas como un set.
Eliminar Contacto: Permite al usuario eliminar un contacto existente por nombre.
Buscar Contacto: Permite al usuario buscar un contacto por nombre y mostrar la información del contacto.
Listar Contactos por Etiquetas: Muestra todos los contactos organizados por etiquetas, usando sets para evitar etiquetas duplicadas.
Ejemplo de Uso
Agregar contacto: Juan Pérez, 123456789, etiquetas: ['amigo', 'trabajo']
Buscar contacto: Juan Pérez
Eliminar contacto: Juan Pérez
Listar contactos por etiquetas: amigo: Juan Pérez, María López
Requisitos
Implementar funciones para cada una de las funcionalidades mencionadas.
Asegurarte de manejar adecuadamente los casos en los que no existan contactos, o cuando se busque uno que no esté en la lista.

'''

class ListaDeContactos:
    def __init__(self) -> None:
        self.lista_contactos = []
        
    def agregar_contacto(self, contacto):
        self.lista_contactos.append(contacto)
    
    def eliminar_contacto():
        pass
class Contacto:
    def __init__(self):
        self.nombre
        self.telefono
        self.etiqueta