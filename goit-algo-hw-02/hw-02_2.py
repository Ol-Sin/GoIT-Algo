from collections import deque

def is_palindrome(s):
    # Конвертуємо рядок до нижнього регістру та прибираємо пробіли та інші неалфавітні символи
    cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Додаємо символи до двосторонньої черги
    char_deque = deque(cleaned_s)
    
    # Визначаємо половину довжини черги
    half_deque = len(char_deque) // 2
    
    # Отримуємо префікс та суфікс черги
    pref_deque = deque()
    for _ in range(half_deque):
        pref_deque.append(char_deque.popleft())
    
    suff_deque = deque()
    for _ in range(half_deque):
        suff_deque.append(char_deque.pop())

    # Порівнюємо префікс та суфікс
    return pref_deque == suff_deque

# Приклад використання
input_string = "A man a plan a canal Panama"
if is_palindrome(input_string):
    print(f"'{input_string}' є паліндромом")
else:
    print(f"'{input_string}' не є паліндромом")
