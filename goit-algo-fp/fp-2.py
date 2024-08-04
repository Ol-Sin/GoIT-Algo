import turtle
import math

def draw_branch(t, length, level):
    if level == 0:
        return

    # Намалювати основну гілку
    t.forward(length)

    # Перейти до кінця гілки
    t.left(45)
    draw_branch(t, length / math.sqrt(2), level - 1)
    t.right(90)
    draw_branch(t, length / math.sqrt(2), level - 1)
    t.left(45)

    # Повернутися до початкового положення
    t.backward(length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    tree = turtle.Turtle()
    tree.speed(0)
    tree.penup()
    tree.goto(0, -200)  # Початкова позиція
    tree.pendown()
    tree.left(90)
    
    # Запитати у користувача рівень рекурсії
    level = int(screen.numinput("Вхідні дані", "Введіть рівень рекурсії (наприклад, 5):", minval=1, maxval=10))
    
    # Малюємо фрактал
    draw_branch(tree, 100, level)
    
    turtle.done()

if __name__ == "__main__":
    main()
