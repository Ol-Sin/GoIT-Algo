import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка функції та області інтегрування
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло для обчислення інтегралу
N = 10000  # Кількість випадкових точок
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, max(y), N)

# Обчислення кількості точок під кривою
under_curve = y_rand < f(x_rand)
integral_mc = (b - a) * max(y) * np.sum(under_curve) / N

# Аналітичний розрахунок інтегралу
integral_analytic, _ = quad(f, a, b)

# Виведення результатів
print(f'Обчислення методом Монте-Карло: {integral_mc}')
print(f'Аналітичний розрахунок: {integral_analytic}')
print(f'Різниця: {abs(integral_mc - integral_analytic)}')

# Візуалізація методу Монте-Карло
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Метод Монте-Карло для інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))

# Додавання випадкових точок на графік
ax.scatter(x_rand, y_rand, c='blue', s=1, alpha=0.5)
ax.scatter(x_rand[under_curve], y_rand[under_curve], c='green', s=1, alpha=0.5)

plt.grid()
plt.show()
