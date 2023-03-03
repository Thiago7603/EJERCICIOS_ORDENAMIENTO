def redixsort(arr):
    # encontrar el número máximo para determinar el número de dígitos
    max_num = max(arr)
    digits = len(str(max_num))
    
    # ordenar por cada dígito, de menos significativo a más significativo
    for i in range(digits):
        # inicializar las listas para cada dígito
        buckets = [[] for j in range(10)]
        # dividir los números en los buckets correspondientes
        for num in arr:
            digit = (num // (10**i)) % 10
            buckets[digit].append(num)
        # reconstruir la lista en orden
        arr = [num for bucket in buckets for num in bucket]
    
    return arr