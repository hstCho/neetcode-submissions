# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index_set = set()
        i = 0
        while head:
            if head in index_set:
                return True
            index_set.add(head)
            head = head.next
        return False