import time
import sys

sys.setrecursionlimit(10000)

def bubble_sort(arr):
    n = len(arr)
    comparaciones = 0
    intercambios = 0
    tiempo_inicio = time.time()
    
    for i in range(n):
        for j in range(0, n-i-1):
            comparaciones += 1
            if arr[j] < arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambios += 1
                
    tiempo_fin = time.time()
    return {
        'tiempo': tiempo_fin - tiempo_inicio,
        'comparaciones': comparaciones,
        'intercambios': intercambios
    }

def insertion_sort(arr):
    n = len(arr)
    comparaciones = 0
    intercambios = 0
    tiempo_inicio = time.time()
    
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0:
            comparaciones += 1
            if arr[j] < key:  
                arr[j + 1] = arr[j]
                intercambios += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
        
    tiempo_fin = time.time()
    return {
        'tiempo': tiempo_fin - tiempo_inicio,
        'comparaciones': comparaciones,
        'intercambios': intercambios
    }

def merge_sort_recursivo(arr):
    stats = {'comparaciones': 0, 'intercambios': 0}
    
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            stats['comparaciones'] += 1
            if left[i] >= right[j]: 
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            stats['intercambios'] += 1
            
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

def merge_sort_iterativo(arr):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            stats['comparaciones'] += 1
            if left[i] >= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            stats['intercambios'] += 1
            
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    tiempo_inicio = time.time()
    stats = {'comparaciones': 0, 'intercambios': 0}
    
    size = 1
    n = len(arr)
    
    while size < n:
        for left in range(0, n, 2*size):
            mid = min(left + size, n)
            right = min(left + 2*size, n)
            if mid < right:
                left_half = arr[left:mid]
                right_half = arr[mid:right]
                merged = merge(left_half, right_half)
                arr[left:right] = merged
        size *= 2
        
    tiempo_fin = time.time()
    stats['tiempo'] = tiempo_fin - tiempo_inicio
    return stats

def quicksort_recursivo(arr):
    stats = {'comparaciones': 0, 'intercambios': 0}
    
    def partition(arr, low, high):
        mid = (low + high) // 2
        if arr[low] < arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
            stats['intercambios'] += 1
        if arr[low] < arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
            stats['intercambios'] += 1
        if arr[mid] < arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]
            stats['intercambios'] += 1
            
        pivot = arr[mid]
        arr[mid], arr[high-1] = arr[high-1], arr[mid]
        stats['intercambios'] += 1
        
        i = low
        j = high - 1
        
        while True:
            i += 1
            while arr[i] > pivot: 
                stats['comparaciones'] += 1
                i += 1
            
            j -= 1
            while arr[j] < pivot:  
                stats['comparaciones'] += 1
                j -= 1
                
            if i >= j:
                break
                
            arr[i], arr[j] = arr[j], arr[i]
            stats['intercambios'] += 1
            
        arr[i], arr[high-1] = arr[high-1], arr[i]
        stats['intercambios'] += 1
        return i

    def insertion_sort(arr, low, high):
        for i in range(low + 1, high + 1):
            key = arr[i]
            j = i - 1
            while j >= low and arr[j] < key:
                stats['comparaciones'] += 1
                arr[j + 1] = arr[j]
                stats['intercambios'] += 1
                j -= 1
            arr[j + 1] = key

    def quicksort(arr, low, high):
        if high - low <= 10:
            insertion_sort(arr, low, high)
            return

        if low < high:
            pivot_index = partition(arr, low, high)
            if pivot_index - low < high - pivot_index:
                quicksort(arr, low, pivot_index - 1)
                quicksort(arr, pivot_index + 1, high)
            else:
                quicksort(arr, pivot_index + 1, high)
                quicksort(arr, low, pivot_index - 1)

    tiempo_inicio = time.time()
    quicksort(arr, 0, len(arr) - 1)
    tiempo_fin = time.time()
    
    stats['tiempo'] = tiempo_fin - tiempo_inicio
    return stats

def quicksort_iterativo(arr):
    stats = {'comparaciones': 0, 'intercambios': 0}
    
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            stats['comparaciones'] += 1
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                stats['intercambios'] += 1
                
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        stats['intercambios'] += 1
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