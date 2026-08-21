# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #step0: prev = null
        #step1 : remember next
        #step2 : reverse the arrows for current -> curr.next = prev
        #step3 : prev = curr, curr = next
        #step 4 : repeat till curr = NULL

        prev = None
        current = head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev
