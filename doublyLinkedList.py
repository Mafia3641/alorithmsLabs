class Node:
    def __init__(self, prev=None, next=None, value=None):
        self.value = value
        self.next = next
        self.prev = prev
    
    def set_next(self, value, prev=None):
        self.next = Node(value=value, prev=prev)
    
    def set_prev(self, value):
        self.prev = Node(value)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.prev = None
        self._length = 0
    
    def is_empty(self):
        return self.head is None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    @property
    def length(self):
        return self._length
    
    def add_tail_node(self, value):
        if self.is_empty():
            self.head = Node(value=value)
        else:
            for last_node in self:
                pass
            last_node.next = Node(value=value, prev=last_node)
        self._length += 1

    def insert_at_head(self, value):
        if self.is_empty():
            self.head = Node(value=value)
        else:
            new_node = Node(value=value, next=self.head)
            self.head.prev = new_node
            self.head = new_node
        self._length += 1
    
    def remove_from_head(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        self._length -= 1
        return temp
    
    def remove_from_tail(self):
        if self.head is None:
            return None
        for last_node in self:
            pass
        if last_node.prev is None:
            return self.remove_from_head()
        temp = last_node
        last_node.prev.next = None
        self._length -= 1
        return temp
    
    def get_node_by_position(self, position):
        """Извлекает ноду по её позиции в списке (начиная с 0)"""
        if position < 0 or position >= self._length:
            print(f"Ошибка: позиция {position} вне диапазона [0, {self._length-1}]")
            return None
        
        print(f"Поиск элемента на позиции {position}:")
        current = self.head
        current_pos = 0
        
        while current is not None:
            if current_pos == position:
                print(f"Найден элемент: {current.value}")
                return current
            
            print(f"  Позиция {current_pos}: {current.value} -> следующая")
            current = current.next
            current_pos += 1
        
        return None


doubly_linked_list = DoublyLinkedList()

def show_pipeline():
    print("Сейчас в списке имеются элементы: ", end='\n\n')
    print("---------------------------")
    print('*начало списка*')
    for i in doubly_linked_list:
        print(i.value)
    else: print("*конец списка*")
    print("--------------------------", end='\n\n')

def show_length():
    print(f"Количество элементов в списке: {doubly_linked_list.length}", end='\n\n')

def test_search():
    """Тестирование поиска по позициям"""
    print("Тестирование поиска по позициям:")
    
    # Тестируем корректные позиции
    for position in [0, 1, 2]:
        print(f"Поиск элемента на позиции {position}:")
        result = doubly_linked_list.get_node_by_position(position)
        if result:
            print(f"На позиции {position} находится: {result.value}")
        print()
    
    # Тестируем некорректную позицию
    print("Попытка поиска на несуществующей позиции 10:")
    result = doubly_linked_list.get_node_by_position(10)
    if not result:
        print("Элемент не найден")
    print()

# Основная программа
print("Проверка работоспособности, проверяем создается ли пустой список: ")
show_pipeline()
show_length()

print("Добавляем объект 456 в начало, теперь список выглядит так: ")
doubly_linked_list.insert_at_head(456)
show_pipeline()
show_length()

print('Теперь попробуем добавить в конец элемент 789: ')
doubly_linked_list.add_tail_node(789)
show_pipeline()
show_length()

print('Теперь добавим новый элемент 123 в начало списка: ')
doubly_linked_list.insert_at_head(123)
show_pipeline()
show_length()

print("Теперь снова добавим в хвост новый элемент 000: ")
doubly_linked_list.add_tail_node('000')
show_pipeline()
show_length()

# Тестирование поиска
test_search()

print("Протестируем удаление с конца: ")
removed = doubly_linked_list.remove_from_tail()
print(f'Удаляем объект {removed.value}')
show_pipeline()
show_length()

# Тестирование поиска после удаления
print("Тестирование поиска после удаления:")
test_search()

# Демонстрация работы с пустым списком
print("Создаем новый пустой список для тестов:")
empty_list = DoublyLinkedList()
print(f"Количество элементов в пустом списке: {empty_list.length}")
empty_list.get_node_by_position(0)