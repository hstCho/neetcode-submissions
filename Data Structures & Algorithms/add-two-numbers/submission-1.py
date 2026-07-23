# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_dict = {}
        cur1, cur2 = l1, l2
        digits = quotient = 0

        while cur1 or cur2:
            if cur1 and not cur2:
                sum_value = cur1.val + quotient
                cur1 = cur1.next
            elif not cur1 and cur2:
                sum_value = cur2.val + quotient
                cur2 = cur2.next
            else:
                sum_value = cur1.val + cur2.val + quotient
                cur1, cur2 = cur1.next, cur2.next
            quotient, remainder = sum_value // 10, sum_value % 10
            new_node = ListNode(remainder, None)
            res_dict[digits] = new_node
            digits += 1
        
        if quotient > 0:
            new_node = ListNode(quotient, None)
            res_dict[digits] = new_node
            digits += 1
        
        for i in range(1, digits):
            res_dict[i-1].next = res_dict[i]

        return res_dict[0]