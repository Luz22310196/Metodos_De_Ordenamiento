def natural_merge_sort(lista):
    runs = []
    run = [lista[0]]

    # Detectar secuencias naturales
    for i in range(1, len(lista)):
        if lista[i] >= lista[i - 1]:
            run.append(lista[i])
        else:
            runs.append(run)
            run = [lista[i]]
    runs.append(run)

    # Fusionar secuencias naturales
    while len(runs) > 1:
        nueva = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                nueva.append(merge(runs[i], runs[i + 1]))
            else:
                nueva.append(runs[i])
        runs = nueva
    return runs[0]

# Ejemplo
datos = [2, 4, 9, 1, 3, 7, 0, 5, 6]
print("Natural Merge Sort:", natural_merge_sort(datos))
