def multiway_merge_sort(lista, k=3):
    # Divide la lista en k partes
    partes = []
    n = len(lista)
    for i in range(0, n, n // k if n // k else 1):
        sublista = sorted(lista[i:i + n // k])
        partes.append(sublista)

    # Fusionar las k listas
    while len(partes) > 1:
        nueva = []
        for i in range(0, len(partes), k):
            nueva.append(multi_merge(partes[i:i + k]))
        partes = nueva
    return partes[0]

def multi_merge(listas):
    resultado = []
    indices = [0] * len(listas)
    while True:
        minimo = None
        idx_min = -1
        for i, l in enumerate(listas):
            if indices[i] < len(l):
                if minimo is None or l[indices[i]] < minimo:
                    minimo = l[indices[i]]
                    idx_min = i
        if idx_min == -1:
            break
        resultado.append(minimo)
        indices[idx_min] += 1
    return resultado

# Ejemplo
datos = [8, 2, 9, 1, 6, 3, 5, 7, 4]
print("Balanced Multiway Merge Sort:", multiway_merge_sort(datos, k=3))
