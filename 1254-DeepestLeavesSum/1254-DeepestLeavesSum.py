# Last updated: 7/16/2025, 9:42:20 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        queue = deque([root])
        
        while queue:
            total = 0
            levelnodes = len(queue)
            for i in queue:
                total += i.val
            for node in range(levelnodes):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return total
        
        
        