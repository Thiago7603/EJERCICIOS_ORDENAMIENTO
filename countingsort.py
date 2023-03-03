def counting_sort(arr):
    # encontrar el valor máximo en el arreglo
    max_value = max(arr)
    
    # inicializar el arreglo de conteo con ceros
    count = [0] * (max_value + 1)
    
    # contar el número de veces que aparece cada elemento
    for num in arr:
        count[num] += 1
    
    # construir el arreglo ordenado
    sorted_arr = []
    for i in range(max_value + 1):
        sorted_arr += [i] * count[i]
        
    return sorted_arr