# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(i):
            prev = None
            cruss = i

            while cruss:
                next_i = cruss.next
                cruss.next = prev
                prev = cruss
                cruss = next_i
        
            return prev
        head = reverse(head)
        return head
        