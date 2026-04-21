# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        middle = ListNode(0)
        if left == right:
            return head

        if left == 1:
            middle = head
            head = None
        
        dummy = head
        count = 0
        while dummy:
            count += 1
            if count + 1== left:
                middle = dummy.next
                dummy.next = None
            dummy = dummy.next
        
        last = ListNode(0)
        ll = middle
        while ll:
            count += 1
            if count == right:
                last = ll.next
                ll.next = None
            ll = ll.next

        prev = None
        curr = middle
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        if head:
            pointer = head
            while pointer.next:
                pointer = pointer.next
            pointer.next = prev
            while pointer.next:
                pointer = pointer.next
            pointer.next = last
            return head
        else:
            pointer = prev
            while pointer.next:
                pointer = pointer.next
            pointer.next = last
            return prev


