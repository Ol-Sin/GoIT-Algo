from queue import Queue
import random
import time

class Request:
    def __init__(self, name):
        self.name = name
        self.actions = random.randint(1, 5)  # Випадкова кількість взаємодій

class ServiceCenter:
    def __init__(self):
        self.requests = Queue()

    def generate_request(self, request):
        self.requests.put(request)
        print(f"Додано заявку: {request.name} з {request.actions} взаємодій")

    def process_request(self):
        while not self.requests.empty():
            current_request = self.requests.get()
            print(f"Обслуговуємо заявку {current_request.name} з {current_request.actions} взаємодій")
            processing_time = random.randint(1, 5)  # Випадковий таймаут на обробку від 1 до 5 секунд
            time.sleep(processing_time)
            print(f"Заявка {current_request.name} оброблена")

# Створюємо Сервісний Центр
sc = ServiceCenter()

# Додаємо заявки
for i in range(15):
    sc.generate_request(Request(f"Request-000{i}"))

# Беремо в роботу заявки
sc.process_request()
