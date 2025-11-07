def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1

        # Mueve los elementos mayores hacia la derecha
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = actual
        print(f"Paso {i}: {lista}")

# Ejemplo de uso
datos = [9, 5, 1, 4, 3]
print("Lista original:", datos)
insertion_sort(datos)
print("Lista ordenada:", datos)
