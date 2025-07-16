# Last updated: 7/16/2025, 9:42:38 AM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        move = [(0,1), (0, -1), (1, 0), (-1, 0)]
        
        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1
        
        def dfs(row, col):
            if (row, col) in seen:
                return 0
            seen.add((row,col))
            if not isValid(row, col):
                return 0
            area = 1
            for node in move:
                nextrow = row + node[0]
                nextcol = col + node[1]
                area += dfs(nextrow, nextcol)
            return area
        
        seen = set()
        ans = 0
        
        for row in range(m):
            for col in range(n):
                ans = max(ans, dfs(row, col))
        
        return ans
        