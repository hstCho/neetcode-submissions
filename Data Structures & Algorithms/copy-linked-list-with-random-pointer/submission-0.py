"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_dict = {None: None}

        curr = head
        while curr:
            new_node = Node(curr.val, None, None)
            node_dict[curr] = new_node
            curr = curr.next
        
        curr_node = head
        while curr_node:
            new_node = node_dict[curr_node]
            new_node.next = node_dict[curr_node.next]
            new_node.random = node_dict[curr_node.random]
            curr_node = curr_node.next
        
        return node_dict[head]
