class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

# Array of index w/ singly linked list 
class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
    
    def hash_function(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        head = self.table[index]

        if not head:
            self.table[index] = Node(key, value)
        else:
            prev = None
            while head:
                if head.key == key:
                    head.value = value
                    return
                prev, head = head, head.next
            prev.next = Node(key, value)
        self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        head = self.table[index]

        while head:
            if head.key == key:
                return head.value
            head = head.next
        
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        head = self.table[index]
        prev = None

        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next
                else:
                    self.table[index] = head.next
                self.size -= 1
                return True
            prev, head = head, head.next
        
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity


        for node in self.table:
            while node:
                index = node.key % new_capacity
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.value)
                else:
                    new_head = new_table[index]
                    while new_head.next:
                        new_head = new_head.next
                    new_head.next = Node(node.key, node.value)
                node = node.next
                
        self.capacity = new_capacity
        self.table = new_table


