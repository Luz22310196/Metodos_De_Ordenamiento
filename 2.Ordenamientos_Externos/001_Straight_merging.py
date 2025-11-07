def straight_merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    izquierda = straight_merge_sort(lista[:mid])
    derecha = straight_merge_sort(lista[mid:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Ejemplo
datos = [8, 3, 5, 1, 9, 2]
print("Straight Merge Sort:", straight_merge_sort(datos))
