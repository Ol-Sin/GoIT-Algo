class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        sorted_list = LinkedList()
        current = self.head

        while current:
            new_node = Node(current.value)
            if not sorted_list.head or sorted_list.head.value >= new_node.value:
                new_node.next = sorted_list.head
                sorted_list.head = new_node
            else:
                sorted_current = sorted_list.head
                while (sorted_current.next and
                       sorted_current.next.value < new_node.value):
                    sorted_current = sorted_current.next
                new_node.next = sorted_current.next
                sorted_current.next = new_node
            current = current.next

        return sorted_list

    def merge_sorted_lists(self, other):
        dummy = Node(0)
        tail = dummy
        p1 = self.head
        p2 = other.head

        while p1 and p2:
            if p1.value <= p2.value:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next

        if p1:
            tail.next = p1
        if p2:
            tail.next = p2

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')

# Приклад використання
# Створення і заповнення першого списку
ll1 = LinkedList()
ll1.append(4)
ll1.append(2)
ll1.append(3)
ll1.append(1)

print("Оригінальний список:")
ll1.print_list()

# Реверсування першого списку
ll1.reverse()
print("Перевернутий список:")
ll1.print_list()

# Сортування перевернутого списку
sorted_ll1 = ll1.insertion_sort()
print("Відсортований список:")
sorted_ll1.print_list()

# Створення і заповнення другого списку
ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

print("Список 2:")
ll2.print_list()

# Об'єднання відсортованих списків
merged_ll = sorted_ll1.merge_sorted_lists(ll2)
print("Об'єднаний список:")
merged_ll.print_list()
