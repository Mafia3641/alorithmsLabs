class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.heap_size = 0
        self.pos = {}  # словарь для хранения позиций элементов по их ID
    
    def sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][0] < self.heap[parent][0]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                self.pos[self.heap[i][1]] = i
                self.pos[self.heap[parent][1]] = parent
                i = parent
            else:
                break
    
    def sift_down(self, i):
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            min_index = i
            
            if left < self.heap_size and self.heap[left][0] < self.heap[min_index][0]:
                min_index = left
            if right < self.heap_size and self.heap[right][0] < self.heap[min_index][0]:
                min_index = right
                
            if min_index == i:
                break
                
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.pos[self.heap[i][1]] = i
            self.pos[self.heap[min_index][1]] = min_index
            i = min_index
    
    def insert(self, value, op_id):
        """Добавляет элемент в очередь с приоритетом"""
        self.heap.append((value, op_id))
        self.heap_size += 1
        self.pos[op_id] = self.heap_size - 1
        self.sift_up(self.heap_size - 1)
    
    def extract_min(self):
        """Извлекает минимальный элемент из очереди"""
        if self.heap_size == 0:
            return None
        
        min_val, op_id = self.heap[0]
        del self.pos[op_id]
        
        if self.heap_size > 1:
            self.heap[0] = self.heap.pop()
            self.heap_size -= 1
            self.pos[self.heap[0][1]] = 0
            self.sift_down(0)
        else:
            self.heap.pop()
            self.heap_size -= 1
            
        return min_val
    
    def decrease_key(self, op_id, new_value):
        """Уменьшает значение элемента по его ID"""
        if op_id in self.pos:
            idx = self.pos[op_id]
            old_value, op_id = self.heap[idx]
            self.heap[idx] = (new_value, op_id)
            self.sift_up(idx)
            return True
        return False
    
    def is_empty(self):
        """Проверяет, пуста ли очередь"""
        return self.heap_size == 0
    
    def get_size(self):
        """Возвращает размер очереди"""
        return self.heap_size


def validate_input(parts, operation_count):
    """Валидирует ввод пользователя"""
    if not parts:
        return False, "Пустая команда"
    
    operation = parts[0].upper()
    
    if operation == 'A':
        if len(parts) != 2:
            return False, "Ошибка: команда A требует один аргумент (число)"
        try:
            if int(parts[1]) > 109 or -109 > int(parts[1]):
                return False, "Ошибка: аргумент не моожет быть больше 109 (по модулю)"
            int(parts[1])
            return True, ""
        except ValueError:
            return False, "Ошибка: аргумент должен быть целым числом"
    
    elif operation == 'X':
        if len(parts) != 1:
            return False, "Ошибка: команда X не требует аргументов"
        return True, ""
    
    elif operation == 'D':
        if len(parts) != 3:
            return False, "Ошибка: команда D требует два аргумента (id и значение)"
        try:
            op_id = int(parts[1])
            new_value = int(parts[2])
            if op_id < 0 or op_id >= operation_count:
                return False, f"Ошибка: ID операции должен быть в диапазоне [0, {operation_count-1}]"
            return True, ""
        except ValueError:
            return False, "Ошибка: аргументы должны быть целыми числами"
    
    elif operation in ['S', 'H', 'Q']:
        return True, ""
    
    else:
        return False, f"Ошибка: неизвестная команда '{operation}'"


def print_help():
    """Выводит справку по командам"""
    print("\nДоступные команды:")
    print("A <число>    - Добавить элемент в очередь")
    print("X            - Извлечь минимальный элемент")
    print("D <id> <число> - Уменьшить значение элемента с указанным ID")
    print("S            - Показать размер очереди")
    print("H            - Показать эту справку")
    print("Q            - Выйти из программы")
    print("Примеры:")
    print("  A 10       - Добавить число 10")
    print("  D 0 5      - Уменьшить значение элемента с ID=0 до 5")
    print("  X          - Извлечь минимальный элемент\n")


def main():
    pq = PriorityQueue()
    operation_count = 0
    operation_ids = {}  # для отслеживания ID операций добавления
    
    print("Очередь с приоритетами")
    print_help()
    
    while True:
        try:
            user_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nЗавершение работы...")
            break
        
        if not user_input:
            continue
            
        parts = user_input.split()
        operation = parts[0].upper()
        
        # Валидация ввода
        is_valid, error_msg = validate_input(parts, operation_count)
        if not is_valid:
            print(error_msg)
            continue
        
        if operation == 'A':
            value = int(parts[1])
            op_id = operation_count
            pq.insert(value, op_id)
            operation_ids[op_id] = True
            operation_count += 1
            print(f"Элемент {value} добавлен с ID={op_id}")
        
        elif operation == 'X':
            result = pq.extract_min()
            if result is None:
                print("*")
            else:
                print(f"Извлечен минимальный элемент: {result}")
        
        elif operation == 'D':
            op_id = int(parts[1])
            new_value = int(parts[2])
            
            if op_id not in operation_ids:
                print(f"Ошибка: элемент с ID={op_id} не существует или уже удален")
                continue
            
            if pq.decrease_key(op_id, new_value):
                print(f"Значение элемента с ID={op_id} уменьшено до {new_value}")
            else:
                print(f"Ошибка: не удалось уменьшить значение элемента с ID={op_id}")
        
        elif operation == 'S':
            print(f"Текущий размер очереди: {pq.get_size()}")
        
        elif operation == 'H':
            print_help()
        
        elif operation == 'Q':
            print("Завершение работы...")
            break


if __name__ == '__main__':
    main()