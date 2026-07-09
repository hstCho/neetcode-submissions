# Doubly Linked List Node
class Node:
    def __init__(self, val, prev_node = None, next_node = None):
        self.val = val
        self.prev = prev_node
        self.next = next_node

class Deque:
    def __init__(self):
        # Create two dummy nodes before and after the queue
        # None <- head -> tail; head <- tail -> None
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        last_node = self.tail.prev
        new_node = Node(value, last_node, self.tail)
        last_node.next = new_node
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value, self.head, self.head.next)
        self.head.next.prev = new_node
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        pop_node = self.tail.prev
        pop_node.prev.next = self.tail
        self.tail.prev = pop_node.prev

        return pop_node.val
        
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        pop_node = self.head.next
        self.head.next = pop_node.next
        pop_node.next.prev = self.head
        
        return pop_node.val
        
