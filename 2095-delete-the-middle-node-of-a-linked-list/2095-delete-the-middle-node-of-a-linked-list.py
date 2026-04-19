# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            head = head.next
            return head
        slow = head
        fast = head
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        temp.next = None
        temp.next = slow.next
        slow.next = None
        return head
        