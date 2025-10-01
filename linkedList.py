class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def set_next(self, value):
        self.next = Node(value)


class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_tail_node(self, node):
        if self.head == None:
            self.head = node
            return
        for c in self:
            pass
        c.set_next(node)

    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp


linked_list = LinkedList()
linked_list.insert_at_head(456)
linked_list.add_tail_node(890)
linked_list.insert_at_head(123)
linked_list.add_tail_node(643)

for i in linked_list:
    print(i.value)

while linked_list.head is not None:
    print(f"Мы удаляем объект: {linked_list.remove_from_head().value}")
    print("Остались элементы:")
    for i in linked_list:
        print(i.value)
    print(end='\n')