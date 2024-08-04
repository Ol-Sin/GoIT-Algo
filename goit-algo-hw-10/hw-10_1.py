from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

# Створюємо модель
model = LpProblem("Optimize_Beverage_Production", LpMaximize)

# Визначаємо змінні рішення
# Кількість лимонаду
limonade = LpVariable("Limonade", lowBound=0, cat='Integer')
# Кількість фруктового соку
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Додаємо обмеження
model += 2 * limonade + 1 * fruit_juice <= 100, "Water_Constraint"  # Обмеження на воду
model += 1 * limonade <= 50, "Sugar_Constraint"  # Обмеження на цукор
model += 1 * limonade <= 30, "Lemon_Juice_Constraint"  # Обмеження на лимонний сік
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"  # Обмеження на фруктове пюре

# Додаємо цільову функцію
model += lpSum([limonade, fruit_juice]), "Total_Production"

# Розв'язуємо модель
model.solve()

# Виводимо результати
print(f"Optimal production of Limonade: {value(limonade)} units")
print(f"Optimal production of Fruit Juice: {value(fruit_juice)} units")
print(f"Total production: {value(model.objective)} units")
