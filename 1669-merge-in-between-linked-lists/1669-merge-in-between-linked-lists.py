# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        last = ListNode(0)
        count = -1
        dummy = list1
        while dummy:
            count +=1
            if count + 1 == a:
                last = dummy.next
                dummy.next = None
                break
            dummy = dummy.next
        
        while count < b:
            count += 1
            last = last.next
        
        dummy.next = list2
        while dummy.next:
            dummy = dummy.next
        dummy.next = last
        return list1