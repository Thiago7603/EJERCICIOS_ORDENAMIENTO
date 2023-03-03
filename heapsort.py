def heapify(arr, n, i):
    # Función para convertir un subárbol en un árbol heap
    largest = i  # Inicializar el valor más grande como la raíz
    l = 2 * i + 1  # Izquierda = 2*i + 1
    r = 2 * i + 2  # Derecha = 2*i + 2

    # Ver si el hijo izquierdo del nodo raíz existe y es más grande que la raíz
    if l < n and arr[i] < arr[l]:
        largest = l

    # Ver si el hijo derecho del nodo raíz existe y es más grande que la raíz
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Cambiar la raíz si es necesario
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Heapify el subárbol afectado
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    # Construir un árbol heap (reorganizar el arreglo)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

    return arr