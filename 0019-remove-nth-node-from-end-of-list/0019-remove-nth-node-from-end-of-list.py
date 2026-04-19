# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            head = None
            return head

        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        p = count - n -1
        ll = head
        cnt = 0
        while cnt < p:
            ll = ll.next
            cnt += 1
        if p < 0:
            head = head.next

        if ll and ll.next:
            ll.next = ll.next.next
        return head

