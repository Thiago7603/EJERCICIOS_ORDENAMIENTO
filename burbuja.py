#Ordenamiento Vectorial Metodo BURBUJA


def bubble_sort(arr):
  n = len(arr)
  # Recorre todo el arreglo
  for i in range(n):
    # Realiza comparaciones con los elementos adyacentes y los intercambia si están en orden incorrecto
    for j in range(n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr


# La complejidad del método de Burbuja es O(n^2) ya que necesita recorrer todo el arreglo en el peor caso, (cuando el arreglo está desordenado) y realiza comparaciones para cada par de elementos adyacentes.


# Ordenamineto utilizando el método de Inserción.
def insertion_sort(arr):
  n = len(arr)
  # Recorre todo el arreglo
  for i in range(1, n):
    key = arr[i]
    j = i - 1
    # Mueve los elementos mayores a la derecha de la posición actual
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    # Inserta el elemento en la posición correcta
    arr[j + 1] = key
  return arr


# La complejidad del método de Ordenamiento de Inserción es también O(n^2) en el peor caso, pero en la práctica, suele ser más rápido que Burbuja ya que realiza menos intercambio.

#¿cuál es más eficiente? En general, el método de Inserción es más eficiente que el de Burbuja en la mayoría de los casos. Por ejemplo, el tiempo de ejecución en diferentes tamaños de arreglos, el uso de memoria, la estabilidad del ordenamiento.
