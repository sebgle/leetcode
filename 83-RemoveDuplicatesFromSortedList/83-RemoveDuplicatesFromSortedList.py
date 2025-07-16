# Last updated: 7/16/2025, 9:43:10 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = head
        fast = head
        while fast.next:
            fast = fast.next
            if slow.val == fast.val:
                slow.next = fast.next
            else:
                slow = fast
        return head
            
                