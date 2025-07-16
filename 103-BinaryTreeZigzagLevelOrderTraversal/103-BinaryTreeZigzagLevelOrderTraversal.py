# Last updated: 7/16/2025, 9:43:05 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        zig = True
        queue = deque([root])
        while queue:
            numnodes = len(queue)
            zig = not zig
            temp = []
            for i in range(numnodes):
                if not zig:
                    node = queue.popleft()
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if zig:
                    node = queue.pop()
                    temp.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
            ans.append(temp)
        return ans
                
        