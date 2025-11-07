def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        menores = [x for x in lista if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista if x > pivote]
        return quicksort(menores) + iguales + quicksort(mayores)

# Ejemplo
datos = [8, 3, 1, 7, 0, 10, 2]
print("Lista original:", datos)
resultado = quicksort(datos)
print("Lista ordenada:", resultado)
