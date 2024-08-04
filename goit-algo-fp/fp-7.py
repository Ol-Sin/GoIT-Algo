import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_simulations):
    # Лічильник для кожної можливої суми
    sum_counts = {i: 0 for i in range(2, 13)}

    # Симуляція кидків кубиків
    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sum_counts[roll_sum] += 1

    # Обчислення ймовірностей
    probabilities = {sum_value: count / num_simulations * 100 for sum_value, count in sum_counts.items()}

    return probabilities

def plot_probabilities(monte_carlo_probabilities):
    # Аналітичні ймовірності
    analytical_probabilities = {
        2: 1/36 * 100,
        3: 2/36 * 100,
        4: 3/36 * 100,
        5: 4/36 * 100,
        6: 5/36 * 100,
        7: 6/36 * 100,
        8: 5/36 * 100,
        9: 4/36 * 100,
        10: 3/36 * 100,
        11: 2/36 * 100,
        12: 1/36 * 100
    }

    # Підготовка даних для графіка
    x = list(analytical_probabilities.keys())
    y_analytical = [analytical_probabilities[i] for i in x]
    y_monte_carlo = [monte_carlo_probabilities.get(i, 0) for i in x]

    # Створення графіка
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_analytical, label='Аналітичні ймовірності', marker='o')
    plt.plot(x, y_monte_carlo, label='Ймовірності Монте-Карло', marker='x')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність (%)')
    plt.title('Порівняння ймовірностей сум при киданні двох кубиків')
    plt.legend()
    plt.grid(True)
    plt.xticks(x)
    plt.show()

# Кількість симуляцій
num_simulations = 100000

# Симуляція і обчислення ймовірностей
monte_carlo_probabilities = simulate_dice_rolls(num_simulations)

# Виведення результатів
print("Ймовірності Монте-Карло:")
for sum_value, probability in monte_carlo_probabilities.items():
    print(f"Сума {sum_value}: {probability:.2f}%")

# Візуалізація результатів
plot_probabilities(monte_carlo_probabilities)
