def bubble_sort_reverse(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

def insertion_sort_reverse(arr):
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def selection_sort_reverse(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        max_idx = i
        for j in range(i):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

def merge_sort_reverse(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort_reverse(L)
        merge_sort_reverse(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Lista de números a ordenar
numbers = [6,11, 12, 1, 0, 4, 5, 10, 7, 9, 2, 3, 8]

# Aplicar los algoritmos de ordenamiento
bubble_sort_reverse(numbers)
insertion_sort_reverse(numbers)
selection_sort_reverse(numbers)
merge_sort_reverse(numbers)

print("Lista ordenada de menor a mayor:", numbers)