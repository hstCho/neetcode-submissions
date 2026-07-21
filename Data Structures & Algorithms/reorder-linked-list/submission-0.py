# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_dict = {}
        pos = 0
        while head:
            node_dict[pos] = head
            head = head.next
            pos += 1
        
        for i in range(pos//2):
            node_dict[i].next = node_dict[pos-1-i]
            node_dict[pos-1-i].next = node_dict[i+1]
        
        node_dict[pos//2].next = None
