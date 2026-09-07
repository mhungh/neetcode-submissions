# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None or head.next == None:
            return False
        slow = head.next
        fast = head.next.next

        while fast != None:
            slow = slow.next
            if fast.next == None:
                break
            fast = fast.next.next
            if slow == fast:
                return True
        return False