import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def generate_color(step, total_steps):
    # Генерує колір у 16-ричному форматі, змінюючи яскравість
    ratio = step / total_steps
    red = int(255 * ratio)
    green = int(255 * (1 - ratio))
    blue = 128
    return f'#{red:02X}{green:02X}{blue:02X}'

def visualize_traversal(tree_root, traversal_type):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    # Ініціалізація кольорів для обходу
    step = 0
    total_steps = len(tree.nodes())
    colors = {node: generate_color(step, total_steps) for step, node in enumerate(tree.nodes())}
    
    # Виконання обходу
    visited_order = []
    if traversal_type == "DFS":
        stack = [tree_root]
        visited = set()
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                visited_order.append(node)
                tree.nodes[node.id]['color'] = colors[node.id]
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
    elif traversal_type == "BFS":
        queue = deque([tree_root])
        visited = set()
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                visited_order.append(node)
                tree.nodes[node.id]['color'] = colors[node.id]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    # Вивід порядку відвідування
    print(f'{traversal_type} Order of Visit:')
    for node in visited_order:
        print(f'Node {node.val} (ID: {node.id})')

    # Візуалізація графу
    node_colors = [tree.nodes[node]['color'] for node in tree.nodes()]
    labels = {node: tree.nodes[node]['label'] for node in tree.nodes()}
    
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.title(f'Tree Visualization - {traversal_type}')
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення обходів дерева
visualize_traversal(root, "DFS")  # Для обходу у глибину
visualize_traversal(root, "BFS")  # Для обходу в ширину
