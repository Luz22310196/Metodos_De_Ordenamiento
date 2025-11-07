def selection_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j

        # Intercambio
        lista[i], lista[min_index] = lista[min_index], lista[i]
        print(f"Paso {i+1}: {lista}")

# Ejemplo de uso
datos = [7, 4, 9, 1, 3]
print("Lista original:", datos)
selection_sort(datos)
print("Lista ordenada:", datos)
