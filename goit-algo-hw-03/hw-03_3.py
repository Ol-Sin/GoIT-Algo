# Функція для задачі про Ханойські башти. n - кількість дисків, source - початковий, target - цільовий, auxiliary - допоміжний стержень, towers - словник для стану башт
def hanoi_tower(n, source, target, auxiliary, towers):

    if n == 1:
        disk = towers[source].pop()
        towers[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {towers}")
        return

    hanoi_tower(n - 1, source, auxiliary, target, towers)
    disk = towers[source].pop()
    towers[target].append(disk)
    print(f"Перемістити диск з {source} на {target}: {disk}")
    print(f"Проміжний стан: {towers}")
    hanoi_tower(n - 1, auxiliary, target, source, towers)

def main():
    n = 3  # Кількість дисків
    towers = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }
    print(f"Початковий стан: {towers}")
    hanoi_tower(n, 'A', 'C', 'B', towers)
    print(f"Кінцевий стан: {towers}")

# Виклик функції
main()
