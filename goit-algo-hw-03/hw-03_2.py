import turtle

def koch_curve(t, order, size): # Функція для малювання кривої Коха. t - об'єкт turtle для малювання, order - порядок рекурсії, size - довжина сторони кривої

    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def koch_snowflake(t, order, size): # Функція для малювання сніжинки Коха шляхом з'єднання трьох кривих Коха. t -об'єкт turtle для малювання, order - порядок рекурсії, size - довжина сторони сніжинки

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def draw_koch_snowflake(order, size=300): # Функція для налаштування вікна. order - порядок рекурсії, size - довжина сторони сніжинки (за замовчуванням 300)

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.penup()
    t.goto(-size / 2, size / 3)  # Початкова позиція для малювання
    t.pendown()

    koch_snowflake(t, order, size)

    window.mainloop()

if __name__ == "__main__":
    order = int(input("Введіть рівень рекурсії: ")) # Обережно з великими числами рівня рекурсії, оптимальне значення - 3
    draw_koch_snowflake(order)
