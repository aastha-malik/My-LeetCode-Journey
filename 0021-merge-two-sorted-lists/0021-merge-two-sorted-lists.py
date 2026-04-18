# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        ll = head
        while list1 and list2:

            if list1.val > list2.val:
                ll.next = list2
                list2 = list2.next

            elif list1.val <= list2.val:
                ll.next = list1
                list1 = list1.next
            ll = ll.next
            
        if list1:
            ll.next = list1
        if list2:
            ll.next = list2
        return head.next



        