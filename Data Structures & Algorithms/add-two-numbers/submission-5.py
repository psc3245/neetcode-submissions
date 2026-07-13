# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ""
        carry = False
        while l1 or l2:
            result = 0
            if l1:
                result += l1.val
                l1 = l1.next
            if l2:
                result += l2.val
                l2 = l2.next

            if carry:
                result += 1
                carry = False
            if result > 9:
                result -= 10
                carry = True
            res += str(result)
        
        if carry:
            res += str(1)
        head = ListNode(val=int(res[0]))
        res = res[1:]
        curr = head
        for c in res:
            curr.next = ListNode(val=int(c))
            curr = curr.next
        return head

        
