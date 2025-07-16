# Last updated: 7/16/2025, 9:42:03 AM
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        wall, space = '+', '.'
        m, n = len(maze), len(maze[0])
        
        def isValidMove(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] != wall
        
        def isExit(row, col):
            if row == entrance[0] and col == entrance[1]:
                return False
            return (row == 0 or row == m-1) or (col == 0 or col == n-1)
        
        queue = deque([(entrance[0], entrance[1], 0)])
        seen = {(entrance[0], entrance[1])}
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while queue:
            row, col, steps = queue.popleft()
            if isExit(row, col):
                return steps
            for dx,dy in directions:
                nextrow, nextcol = row+dx, col+dy
                if isValidMove(nextrow, nextcol) and (nextrow,nextcol) not in seen:
                    seen.add((nextrow, nextcol))
                    queue.append((nextrow, nextcol, steps + 1))
        
        return -1 
        
        
        
        
        