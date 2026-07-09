# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        nextNode = head.next
        head.next = None
        prev = head
        head = nextNode
        
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode

        return prev
