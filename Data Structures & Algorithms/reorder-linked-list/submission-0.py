# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        ctr = 0
        curr = head
        while curr:
            ctr += 1
            curr = curr.next

        mid = head
        for _ in range((ctr + 1) // 2 - 1):
            mid = mid.next
        l2 = mid.next
        mid.next = None
        l2 = self.reverse(l2)

        l1 = head
        while l1 and l2:
            t1, t2 = l1.next, l2.next
            l1.next = l2
            l2.next = t1
            l1, l2 = t1, t2
        

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        return prev