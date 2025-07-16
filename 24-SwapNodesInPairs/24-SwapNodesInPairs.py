# Last updated: 7/16/2025, 9:43:12 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        newhead = head.next
        temp = head.next.next
        head.next.next = head
        head.next = self.swapPairs(temp)
        return newhead