import heapq
import random

def min_cost_to_connect_cables(cables):
    if len(cables) == 0:
        return 0

    # Створюємо мін-кучу з довжин кабелів
    heapq.heapify(cables)
    print("Початкова купа:", cables)

    total_cost = 0

    # Поки в купі більше одного кабелю
    while len(cables) > 1:
        # Виймаємо два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Вартість їх з'єднання
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад до купи
        heapq.heappush(cables, cost)

        print(f"З'єднали {first} і {second}, витрати: {cost}. Поточна купа:", cables)

    return total_cost

# Приклад використання
cables = random.sample(range(1, 21), 10)
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))
