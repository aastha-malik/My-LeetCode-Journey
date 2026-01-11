# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None

        p = None
        c = slow
        while c:
            temp = c.next
            c.next = p
            p = c
            c = temp
            
        f = head
        s = p
        while f and s:
            f1 = f.next
            p1 = s.next
            f.next = s
            if f1:
                s.next = f1
            f = f1
            s = p1