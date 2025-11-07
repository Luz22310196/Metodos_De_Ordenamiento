class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    if valor < raiz.valor:
        raiz.izq = insertar(raiz.izq, valor)
    else:
        raiz.der = insertar(raiz.der, valor)
    return raiz

def en_orden(raiz, lista):
    if raiz:
        en_orden(raiz.izq, lista)
        lista.append(raiz.valor)
        en_orden(raiz.der, lista)

def tree_sort(lista):
    raiz = None
    for valor in lista:
        raiz = insertar(raiz, valor)
    lista_ordenada = []
    en_orden(raiz, lista_ordenada)
    return lista_ordenada

# Ejemplo
datos = [5, 2, 9, 1, 7]
print("Lista original:", datos)
resultado = tree_sort(datos)
print("Lista ordenada:", resultado)
