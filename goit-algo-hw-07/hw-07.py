import random
from anytree import Node, RenderTree

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def insert(root, key): # Додавання вузла
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def find_max_value(node): # Пошук максимального значення
    current = node
    while current.right is not None:
        current = current.right
    return current.key

def find_min_value(node): # Пошук мінімального значення
    current = node
    while current.left is not None:
        current = current.left
    return current.key

def find_sum(node): # Сума всіх значень
    if node is None:
        return 0
    return node.key + find_sum(node.left) + find_sum(node.right)

def is_balanced(node): # Перевірка дарава на збалансованість
    if not node:
        return True
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    if abs(left_height - right_height) > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)

def build_anytree(node, parent=None): # Побудова дерева
    if node is None:
        return None
    tree_node = Node(str(node.key), parent=parent)
    build_anytree(node.left, tree_node)
    build_anytree(node.right, tree_node)
    return tree_node

# Створення дерева
root = None
keys = random.sample(range(-10, 11), 10)

for key in keys:
    root = insert(root, key)
    print("Вставлено:", key)

# Використовуємо anytree для візуалізації
tree = build_anytree(root)
print("AVL-Дерево:")
for pre, fill, node in RenderTree(tree):
    print("%s%s" % (pre, node.name))

# Пошук максимального, мінімального значень та суми
max_value = find_max_value(root)
min_value = find_min_value(root)
sum_values = find_sum(root)

print("Найбільше значення в дереві:", max_value)
print("Найменше значення в дереві:", min_value)
print("Сума всіх значень у дереві:", sum_values)

# Перевірка дерева на збалансованість
if is_balanced(root):
    print("Дерево збалансоване")
else:
    print("Дерево не збалансоване")
