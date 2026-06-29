# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        tail = head
        dif = 0
        while (dif < n):
            fast = fast.next
            dif += 1
        
        if fast == None:
            return head.next
        
        while fast.next:
            fast = fast.next
            tail = tail.next
        
        tail.next = tail.next.next

        return head
