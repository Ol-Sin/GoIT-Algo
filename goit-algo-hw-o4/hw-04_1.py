import random
import timeit

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Сортування вставкою
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Обгортка для Timsort (вбудоване сортування)
def timsort(arr):
    return sorted(arr)

# Генерація випадкових чисел для сортування
def generate_data(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Функція для вимірювання часу сортування
def time_sorting_algorithm(algorithm, data):
    timer = timeit.Timer(lambda: algorithm(data.copy()))
    return timer.timeit(number=1)

# Різні набори даний для тестування
data_sizes = [100, 1000, 10000]

# Сортування з заміром часу
for size in data_sizes:
    data = generate_data(size)
    print(f"Data size: {size}")
    
    merge_sort_time = time_sorting_algorithm(merge_sort, data)
    print(f"Merge Sort: {merge_sort_time:.6f} seconds")
    
    insertion_sort_time = time_sorting_algorithm(insertion_sort, data)
    print(f"Insertion Sort: {insertion_sort_time:.6f} seconds")
    
    timsort_time = time_sorting_algorithm(timsort, data)
    print(f"Timsort: {timsort_time:.6f} seconds")
    print()


# На основі цих тестів випадкових даних можна зробити висновок,
# що Timsort об'єднує найкращі характеристики двох інших алгоритмів,
# забезпечуючи високу ефективність для різних типів наборів даних.
# Саме тому зручніше використовувати вбудовані функції сортування в Python, такі як sorted, а не створювати свої власні алгоритми.