import time

def bubble_sort(arr, comparator):
    n = len(arr)
    tiempo_inicio = time.time()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if comparator.compare(arr[j], arr[j + 1]) == 1:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    tiempo_fin = time.time()
    return {
        'tiempo': tiempo_fin - tiempo_inicio
    }

def insertion_sort(arr, comparator):
    n = len(arr)
    tiempo_inicio = time.time()
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and comparator.compare(arr[j], key) == 1:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    tiempo_fin = time.time()
    return {
        'tiempo': tiempo_fin - tiempo_inicio
    }

def insertion_sort_interno(arr, low, high, comparator):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and comparator.compare(arr[j], key) == 1:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort_recursivo(arr, comparator):
    stats = {'tiempo': 0}
    
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if comparator.compare(left[i], right[j]) == -1:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(arr):
        if len(arr) <= 1:
            return arr
            
        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        return merge(left, right)

    tiempo_inicio = time.time()
    sorted_arr = sort(arr)
    tiempo_fin = time.time()
    
    arr[:] = sorted_arr
    stats['tiempo'] = tiempo_fin - tiempo_inicio
    return stats

def merge_sort_iterativo(arr, comparator):
    stats = {'tiempo': 0}
    
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if comparator.compare(left[i], right[j]) == -1:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    tiempo_inicio = time.time()
    n = len(arr)
    size = 1
    
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            if mid < right:
                left_half = arr[left:mid]
                right_half = arr[mid:right]
                merged = merge(left_half, right_half)
                arr[left:right] = merged
        size *= 2
    
    tiempo_fin = time.time()
    stats['tiempo'] = tiempo_fin - tiempo_inicio
    return stats

def quicksort_recursivo(arr, comparator):
    stats = {'tiempo': 0}
    
    def partition(arr, low, high):
        mid = (low + high) // 2
        if comparator.compare(arr[low], arr[mid]) == 1:
            arr[low], arr[mid] = arr[mid], arr[low]
        if comparator.compare(arr[low], arr[high]) == 1:
            arr[low], arr[high] = arr[high], arr[low]
        if comparator.compare(arr[mid], arr[high]) == 1:
            arr[mid], arr[high] = arr[high], arr[mid]
        
        pivot = arr[mid]
        arr[mid], arr[high - 1] = arr[high - 1], arr[mid]
        
        i = low
        j = high - 1
        
        while True:
            i += 1
            while comparator.compare(arr[i], pivot) == -1:
                i += 1
            j -= 1
            while comparator.compare(arr[j], pivot) == 1:
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
        
        arr[i], arr[high - 1] = arr[high - 1], arr[i]
        return i

    def quicksort(arr, low, high):
        if high - low <= 10: 
            insertion_sort_interno(arr, low, high, comparator)
            return
        
        if low < high:
            pi = partition(arr, low, high)
            quicksort(arr, low, pi - 1)
            quicksort(arr, pi + 1, high)

    tiempo_inicio = time.time()
    quicksort(arr, 0, len(arr) - 1)
    tiempo_fin = time.time()
    
    stats['tiempo'] = tiempo_fin - tiempo_inicio
    return stats

def quicksort_iterativo(arr, comparator):
    stats = {'tiempo': 0}
    
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if comparator.compare(arr[j], pivot) == -1:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    tiempo_inicio = time.time()
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))
    
    tiempo_fin = time.time()
    stats['tiempo'] = tiempo_fin - tiempo_inicio
    return stats