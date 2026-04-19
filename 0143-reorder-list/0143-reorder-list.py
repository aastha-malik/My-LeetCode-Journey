# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            pointer = slow
            slow = slow.next
            fast = fast.next.next
        #slow => one prev node of mid of linked list
        pointer.next = None

        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while head and prev:
            temp1 = head.next
            temp2 = prev.next
            head.next =  prev
            if temp1:
                prev.next = temp1
            head = temp1
            prev = temp2


        
