# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head

        # Reverse the list
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # prev is now the head of the reversed list
        reversed_head = prev

        # Remove the nth node from the beginning
        if n == 1:
            reversed_head = reversed_head.next
        else:
            curr = reversed_head
            for _ in range(n - 2):
                curr = curr.next
            curr.next = curr.next.next

        # Reverse the list again
        prev = None
        curr = reversed_head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev