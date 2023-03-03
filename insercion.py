# ordenamiento vectorial por el método de INSERCION


def insertion_sort(arr):
  n = len(arr)
  # Recorre todo el arreglo
  for i in range(1, n):
    # Inserta el elemento actual en la posición correcta en el subarreglo ordenado
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr


# La complejidad del método de Inserción es O(n^2) en el peor caso ya que necesita recorrer todo el arreglo en el peor caso y mover los elementos hacia la derecha para insertar el elemento actual en la posición correcta en el subarreglo ordenado.


# Ordenamiento de selección
def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr


# La función de complejidad de este algoritmo también es O(n^2) en el peor de los casos.

#¿cuál es más eficiente? En general, En términos de eficiencia, el método de selección y el método de inserción son similares en términos de complejidad. Sin embargo, en la práctica, el método de inserción tiende a ser más rápido para vectores pequeños, mientras que el método de selección puede ser más rápido para vectores grandes. Esto se debe a que el método de selección realiza menos intercambios que el método de inserción.
