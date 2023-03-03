# ordenamiento vectorial por el método de SELECCION

def selection_sort(arr):
    n = len(arr)
    # Recorre todo el arreglo
    for i in range(n):
        # Busca el elemento mínimo en el subarreglo no ordenado
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambia el elemento mínimo con el primer elemento del subarreglo no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# La complejidad del método de Selección es también O(n^2) ya que necesita recorrer todo el arreglo en el peor caso y busca el mínimo en el subarreglo no ordenado para cada posición.


# Ordenamiento de Burbuja con Optimización de Parada Temprana.
def bubble_sort_optimized(arr):
    n = len(arr)
    # Recorre todo el arreglo
    for i in range(n):
        # Realiza comparaciones con los elementos adyacentes y los intercambia si están en orden incorrecto
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Si no se realizaron intercambios en el último recorrido, el arreglo está ordenado
        if not swapped:
            break
    return arr

# La complejidad del método de Burbuja con Optimización de Parada Temprana es también O(n^2) en el peor caso, pero en la práctica suele ser más rápido que Selección ya que puede evitar recorrer todo el arreglo si ya está ordenado.

#¿cuál es más eficiente? En general, el método de Burbuja con Optimización de Parada Temprana es más eficiente que Selección en la mayoría de los casos. Por ejemplo, el tiempo de ejecución en diferentes tamaños de arreglos, el uso de memoria, la estabilidad del ordenamiento. Pero el método de Burbuja con Optimización de Parada Temprana puede ser una buena opción si se sabe que el arreglo está casi ordenado o si se quiere evitar el peor caso de Burbuja.