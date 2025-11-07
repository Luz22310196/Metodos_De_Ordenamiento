def exchange_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
        print(f"Paso {i+1}: {lista}")

# Ejemplo
datos = [7, 2, 9, 1, 5]
print("Lista original:", datos)
exchange_sort(datos)
print("Lista ordenada:", datos)
