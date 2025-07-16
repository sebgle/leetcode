# Last updated: 7/16/2025, 9:42:52 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        ans = root.val
        diff = abs(target - root.val)
        
        def helper(root, target):
            nonlocal ans, diff
            if not root:
                return
            if abs(target - root.val) < diff:
                diff = abs(target - root.val)
                ans = root.val
            if abs(target - root.val) == diff:
                ans = min(root.val, ans)
            if root.left and not root.right:
                helper(root.left, target)
            elif root.right and not root.left:
                helper(root.right, target)
            else:
                helper(root.right, target)
                helper(root.left, target)
        
        helper(root, target)
        return ans
                
        