def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        
        if arr[mid] == x:
            return (iterations, arr[mid])
        elif arr[mid] < x:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            high = mid - 1
    
    if upper_bound is None:
        upper_bound = arr[low] if low < len(arr) else None
    
    return (iterations, upper_bound)

# Тестування функції
sorted_array = [0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 1.2, 1.5, 1.7]
x = 0.65
result = binary_search(sorted_array, x)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")
