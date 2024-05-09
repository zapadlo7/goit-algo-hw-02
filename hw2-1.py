from queue import Queue
import time

# Створити чергу заявок
queue = Queue()

# Функція для створення нових заявок
def generate_request():
    new_request = "New request"
    queue.put(new_request)  # Додати заявку до черги
    print("Generated request:", new_request)

# Функція для обробки заявок
def process_request():
    if not queue.empty():  # Якщо черга не пуста
        request = queue.get()  # Видалити заявку з черги
        print("Processed request:", request)
    else:
        print("Queue is empty")  # Вивести повідомлення, що черга пуста

# Головний цикл програми
while True:
    # Виконати створення нових заявок
    generate_request()
    # Затримка для імітації обробки заявок
    time.sleep(3)
    # Виконати обробку заявок
    process_request()
