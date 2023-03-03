def bucketSort(arr):
    bucket = []
    # crear cubetas vacias
    for i in range(len(arr)):
        bucket.append([])
    # agregar elementos a cubetas
    for j in arr:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    # ordenar elementos de cada cubeta y combinarlas
    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])
    result = []
    for i in range(len(arr)):
        result = result + bucket[i]
    return result
