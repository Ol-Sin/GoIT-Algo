def greedy_algorithm(items, budget):
    # Обчислюємо співвідношення калорій до вартості для кожного елемента
    item_ratios = [(item, details['calories'] / details['cost']) for item, details in items.items()]
    
    # Сортуємо за співвідношенням калорій до вартості (спаданням)
    item_ratios.sort(key=lambda x: x[1], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for item, ratio in item_ratios:
        item_cost = items[item]['cost']
        item_calories = items[item]['calories']
        
        if total_cost + item_cost <= budget:
            selected_items.append(item)
            total_cost += item_cost
            total_calories += item_calories
    
    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    # Ініціалізуємо таблицю для зберігання максимальних калорій для кожного бюджету
    dp = [0] * (budget + 1)
    item_selection = [[] for _ in range(budget + 1)]
    cost_of_selection = [0] * (budget + 1)
    
    for item, details in items.items():
        cost = details['cost']
        calories = details['calories']
        
        # Проходимо таблицю в зворотному порядку, щоб уникнути повторного використання одного елемента
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                item_selection[current_budget] = item_selection[current_budget - cost] + [item]
                cost_of_selection[current_budget] = cost_of_selection[current_budget - cost] + cost
    
    # Максимальні калорії та вибір страв для максимального бюджету
    max_calories = dp[budget]
    selected_items = item_selection[budget]
    total_cost = cost_of_selection[budget]
    
    return selected_items, max_calories, total_cost

# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Розв'язання задачі за допомогою жадібного алгоритму
greedy_items, greedy_calories, greedy_cost = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print(f"Selected items: {greedy_items}")
print(f"Total calories: {greedy_calories}")
print(f"Total cost: {greedy_cost}")

# Розв'язання задачі за допомогою алгоритму динамічного програмування
dp_items, dp_calories, dp_cost = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print(f"Selected items: {dp_items}")
print(f"Total calories: {dp_calories}")
print(f"Total cost: {dp_cost}")
