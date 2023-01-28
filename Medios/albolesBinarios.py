""" 
Un arbol binario es una estructura de datos que se compone de nodos.
Cada nodo puede tener un hijo izquierdo y un hijo derecho.
No puede tener mas de dos hijos por nodo.


"""
lista_test = [68, 5, 3, 23, 4, 3, 2, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95,
              96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 12, 123, 41, 23, 3, 3, 4, 12, 4]


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class Arbol:
    def __init__(self, valor):
        self.raiz = Nodo(valor)

    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)
    
    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end= ", ")
            self.__inorden_recursivo(nodo.derecha)
    
    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end= ", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.dato, end= ", ")
    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)
    
    def inorden(self):
        self.__inorden_recursivo(self.raiz)
    
    def preorden(self):
        self.__preorden_recursivo(self.raiz)
    
    def postorden(self):
        self.__postorden_recursivo(self.raiz)

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)
    

for n, i in enumerate(lista_test):
    if n == 0:
        arbol = Arbol(i)
    else:
        arbol.agregar(i)
        