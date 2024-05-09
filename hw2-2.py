from collections import deque

def is_palindrome(s):
    # Перетворення рядка у нижній регістр та видалення пробілів
    s = s.lower().replace(" ", "")
    # Створення двосторонньої черги
    queue = deque(s)
    
    # Поки черга не пуста і має хоча б один символ
    while len(queue) > 1:
        # Порівняння першого та останнього символів
        if queue.popleft() != queue.pop():
            return False
    return True

# Приклад використання
input_string = "Able was I ere I saw Elba"
print(is_palindrome(input_string))  # Виведе True
