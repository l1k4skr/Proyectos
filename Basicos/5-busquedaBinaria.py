""" Búsqueda binaria 

Dada una lista ordenada tomamos primer y ultimo valor y hacemos una media. ( M = len(lista)//2 )
Asignar 0 a L y a R (n − 1).
Si L > R, la búsqueda termina sin encontrar el valor.
Sea m (la posición del elemento del medio) igual a la parte entera de (L + R) / 2.
Si Am < T, igualar L a m + 1 e ir al paso 2.
Si Am > T, igualar R a m – 1 e ir al paso 2.
Si Am = T, la búsqueda terminó, retornar m.
"""
def bus_Binaria(lista, valor):
    L = 0
        
    R = len(lista) - 1
    if L > R:
        return False
    m = (L + R) // 2
    if lista[m] < valor:
        L = m + 1
        return bus_Binaria(lista[m:], valor)
    elif lista[m] > valor:
        L = m - 1
        return bus_Binaria(lista[:m], valor)
    else:
        
        return m

lista = [1,2,3,4,5,6,7,8,9,10]
print(bus_Binaria(lista, 5))
print(lista[bus_Binaria(lista, 5)])