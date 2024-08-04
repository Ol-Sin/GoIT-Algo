import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}
        self.REMOVED = '<removed-task>'
        self.counter = 0

    def add_task(self, task, priority=0):
        if task in self.entry_finder:
            self.remove_task(task)
        count = self.counter
        self.counter += 1
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.heap, entry)

    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        while self.heap:
            priority, count, task = heapq.heappop(self.heap)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task, priority
        raise KeyError('pop from an empty priority queue')

    def is_empty(self):
        return not self.entry_finder

def dijkstra(graph, start):
    heap = MinHeap()
    heap.add_task(start, 0)
    
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    while not heap.is_empty():
        current_vertex, current_distance = heap.pop_task()
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heap.add_task(neighbor, distance)
    
    return distances

# Приклад використання
if __name__ == "__main__":
    # Визначаємо граф як словник словників
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_vertex = 'A'
    distances = dijkstra(graph, start_vertex)
    
    print("Відстані від вершини", start_vertex)
    for vertex, distance in distances.items():
        print(f"Вершина {vertex}: {distance}")
