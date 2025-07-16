# Last updated: 7/16/2025, 9:43:07 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            ans.append(root.val)
            helper(root.right)
        helper(root)
        return ans
        