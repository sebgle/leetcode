# Last updated: 7/16/2025, 9:42:24 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        result = 0
        
        def helper(root, minn, maxx):
            nonlocal result
            if not root:
                return
            maxx = max(root.val, maxx)
            minn = min(root.val, minn)
            result = max(result, maxx - minn)
            helper(root.left, minn, maxx)
            helper(root.right, minn, maxx)
            
        helper(root, root.val, root.val)
        return result
    
        
        
        