# Last updated: 7/16/2025, 9:43:09 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        if left == right:
            return head
        
        curr = head
        prev = None
        count = 1
        
        while count < left:
            prev = curr
            curr = curr.next
            count += 1

        start = curr
        startprev = prev
        
        while count <= right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1
        
        if not curr and not startprev:
            head = prev
            return head
        
        if not curr:
            startprev.next = prev
            start.next = None
            return head
        
        if not startprev:
            head = prev
            start.next = curr
            return head
        
        start.next = curr
        startprev.next = prev
        
        return head
            