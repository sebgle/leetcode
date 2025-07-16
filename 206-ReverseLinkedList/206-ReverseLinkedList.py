# Last updated: 7/16/2025, 9:42:58 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head, prev):
            if not head:
                return head
            temp = head.next
            head.next = prev
            if temp:
                answer = helper(temp, head)
                return answer
            else:
                return head
        return helper(head, None)