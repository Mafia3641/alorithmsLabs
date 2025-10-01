# class Node:
#     def __init__(self, next=None, prev=None, value=None):
#         self.value = value
#         self.next = next
#         self.prev = prev
    
#     def set_next(self, value):
#         self.next = Node(value)


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def is_empty(self):
#         return self.head is None
    
#     def __iter__(self):
#         node = self.head
#         while node is not None:
#             yield node
#             node = node.next

#     def add_tail_node(self, value):
#         new_node = Node(value)
#         if self.is_empty():
#             self.head = self.tail = new_node
#         else:
#             new_node.prev = self.tail
#         self.tail.next = new_node
#         self.tail = new_node

#     def insert_at_head(self, value):
#         new_node = Node(value)
#         if self.is_empty():
#             self.head = self.tail = new_node
#         else:
#             new_node.next = self.head
        
#         self.head.prev = new_node
#         self.head = new_node
    
#     def remove_from_head(self):
#         if self.head == None:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         return temp


# linked_list = DoublyLinkedList()
# for i in linked_list:
#     print(i)
# linked_list.insert_at_head(456)
# for i in linked_list:
#     print(i)
# linked_list.add_tail_node(890)
# linked_list.insert_at_head(123)
# linked_list.add_tail_node(643)

# for i in linked_list:
#     print(i.value)

# while linked_list.head is not None:
#     print(f"Мы удаляем объект: {linked_list.remove_from_head().value}")
#     print("Остались элементы:")
#     for i in linked_list:
#         print(i.value)
#     print(end='\n')



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
    
    def is_empty(self):
        return self.head is None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def __subscription__(self):
        node = self.head
        while node is not None:
            yield node
            node=node.next
    
    def add_tail_node(self, value):
        if self.is_empty():
            self.head = Node(value=value)
            return
        for last_node in self:
            pass
        last_node.next = Node(value=value, prev=last_node)

    def insert_at_head(self, value):
        if self.is_empty():
            self.head = Node(value=value)
        else:
            new_node = Node(value=value, prev=self.head)
            new_node.next = self.head
            self.head = new_node
    
    def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp
    
    def remove_from_tail(self):
        if self.head == None:
            return None
        for last_node in self:
            pass
        if last_node.prev == None:
            return self.remove_from_head()
        temp = last_node.prev
        temp.next = None
        return last_node


doubly_linked_list = DoublyLinkedList()

# print(f"")
# doubly_linked_list.add_tail_node(890)
# doubly_linked_list.insert_at_head(123)
# doubly_linked_list.add_tail_node(643)

def show_pipeline():
    print("Сейчас в списке имеются элементы: ", end='\n\n')
    print("---------------------------")
    print('*начало списка*')
    for i in doubly_linked_list[::-1]:
        print(i.value)
    else: print("*конец списка*")
    print("--------------------------", end='\n\n')

print("Проверка работоспособности, проверяем создается ли пустой список: ")
show_pipeline()

print("Добавляем объект 456 в начало, теперь список выглядит так: ")
doubly_linked_list.insert_at_head(456)
show_pipeline()

print('Теперь попробуем добавить в конец элемент 789: ')
doubly_linked_list.add_tail_node(789)
show_pipeline()

print('Теперь добавим новый элемент 123 в начало списка: ')
doubly_linked_list.insert_at_head(123)
show_pipeline()

print("Теперь снова добавим в хвост новый элемент 000: ")
doubly_linked_list.add_tail_node('000')
show_pipeline()

print(doubly_linked_list.remove_from_tail().value)

print("Теперь протестируем удаление, будем каждый раз удалять объект сначала с конца, затем с начала: ")
# while doubly_linked_list.head is not None:
#     print(f"Мы удаляем объект: {doubly_linked_list.remove_from_head().value}")
#     print("Остались элементы:")
#     for i in doubly_linked_list:
#         print(i.value)
#     print(end='\n')