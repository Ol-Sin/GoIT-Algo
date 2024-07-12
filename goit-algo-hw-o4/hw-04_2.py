def merge_two_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Додаємо залишок елементів з обох списків
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list

def merge_k_lists(lists):
    if not lists:
        return []

    while len(lists) > 1:
        merged_lists = []
        
        # Зливаємо пари списків
        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i + 1] if (i + 1) < len(lists) else []
            merged_lists.append(merge_two_lists(list1, list2))
        
        # Оновлюємо списки після злиття
        lists = merged_lists
    
    return lists[0] if lists else []

# Приклад використання
lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

merged_list = merge_k_lists(lists)
print(merged_list)
