
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in arr[1:]:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        return quicksort(left) + [pivot] + quicksort(right)

# Generar una lista aleatoria de 10 números enteros
random_list = random.sample(range(100), 10)

# Imprimir la lista original
print("Lista original:", random_list)

# Ordenar la lista con QuickSort
sorted_list = quicksort(random_list)

# Imprimir la lista ordenada
print("Lista ordenada:", sorted_list)